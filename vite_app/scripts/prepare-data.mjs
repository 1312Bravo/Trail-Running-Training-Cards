import { spawnSync } from "node:child_process";
import { existsSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const scriptDirectory = fileURLToPath(new URL(".", import.meta.url));
const repositoryRoot = resolve(scriptDirectory, "../..");
const localPython = resolve(repositoryRoot, ".venv/Scripts/python.exe");
const candidates = process.platform === "win32"
  ? [localPython, "py", "python"]
  : ["python3", "python"];

let result;
for (const command of candidates) {
  if (command === localPython && !existsSync(command)) continue;
  result = spawnSync(command, ["-m", "training_cards.scripts.cache.build_web_bundle"], {
    cwd: repositoryRoot,
    stdio: "inherit",
    shell: process.platform === "win32" && command !== localPython,
  });
  if (!result.error) break;
}

if (!result || result.error || result.status !== 0) {
  process.exit(result?.status ?? 1);
}
