// Renders every uml/**/*.mmd source to uml/rendered/<name>.png (overwrites the old PNG).
// Usage:  npm install   (once)   then   npm run diagrams
// Optional env vars:
//   MMDC_CLI               path to mermaid-cli's src/cli.js (default: local node_modules)
//   MMDC_PUPPETEER_CONFIG  puppeteer JSON config, e.g. {"executablePath":"C:/Program Files/Google/Chrome/Application/chrome.exe"}
import { execFileSync } from 'node:child_process';
import { readdirSync, mkdirSync, statSync } from 'node:fs';
import { join, basename, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const umlDir = join(root, 'uml');
const outDir = join(umlDir, 'rendered');
mkdirSync(outDir, { recursive: true });

// Run mmdc's JS entry point with the current node binary (no shell, so paths with spaces work).
const mmdcCli = process.env.MMDC_CLI || join(root, 'node_modules', '@mermaid-js', 'mermaid-cli', 'src', 'cli.js');

function walk(dir) {
  return readdirSync(dir).flatMap((name) => {
    const p = join(dir, name);
    if (p === outDir) return [];
    return statSync(p).isDirectory() ? walk(p) : p.endsWith('.mmd') ? [p] : [];
  });
}

const sources = walk(umlDir);
for (const src of sources) {
  const out = join(outDir, basename(src, '.mmd') + '.png');
  const args = ['-i', src, '-o', out, '-b', 'white', '-s', '2', '-w', '1600', '-q'];
  if (process.env.MMDC_PUPPETEER_CONFIG) args.push('-p', process.env.MMDC_PUPPETEER_CONFIG);
  execFileSync(process.execPath, [mmdcCli, ...args], { stdio: 'inherit' });
  console.log(`rendered ${src.slice(root.length + 1)} -> ${out.slice(root.length + 1)}`);
}
console.log(`${sources.length} diagram(s) rendered.`);
