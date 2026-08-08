# Day 18 – Shell Scripting: Functions & intermediate Concepts

## Task 1: Basic Functions
1. Create `functions.sh` with:
   - A function `greet` that takes a name as argument and prints `Hello, <name>!`
   - A function `add` that takes two numbers and prints their sum
   - Call both functions from the script
  
[Click here for the script](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-18/script/functions.sh)  

![functios](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-18/images/functions.jpg)
---

## Task 2: Functions with Return Values
1. Create `disk_check.sh` with:
   - A function `check_disk` that checks disk usage of `/` using `df -h`
   - A function `check_memory` that checks free memory using `free -h`
   - A main section that calls both and prints the results

[Click here for the script](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-18/script/disk_check.sh)  

![disk_check](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-18/images/disk_check.jpg)
---

## Task 3: Strict Mode — `set -euo pipefail`
1. Create `strict_demo.sh` with `set -euo pipefail` at the top
2. Try using an **undefined variable** — what happens with `set -u`?
3. Try a command that **fails** — what happens with `set -e`?
4. Try a **piped command** where one part fails — what happens with `set -o pipefail`?

**Document:** What does each flag do?
- `set -e` → Exit immediately if any command returns a non‑zero status. Prevents scripts from continuing after an error.  
- `set -u` → Treats unset variables as errors.  
- `set -o pipefail` → Ensures that in a pipeline (cmd1 | cmd2 | cmd3), the whole pipeline fails if any command fails.  
                       Without this, only the last command’s exit status is checked.

[Click here for the script](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-18/script/strict_demo.sh)  

![local_demo](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-18/images/strict_demo.jpg)

---

## Task 4: Local Variables
1. Create `local_demo.sh` with:
   - A function that uses `local` keyword for variables
   - Show that `local` variables don't leak outside the function
   - Compare with a function that uses regular variables

[Click here for the script](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-18/script/local_demo.sh)  

![local_varo](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-18/images/local-demo.jpg)


---

## Task 5: Build a Script — System Info Reporter
Create `system_info.sh` that uses functions for everything:
1. A function to print **hostname and OS info**
2. A function to print **uptime**
3. A function to print **disk usage** (top 5 by size)
4. A function to print **memory usage**
5. A function to print **top 5 CPU-consuming processes**
6. A `main` function that calls all of the above with section headers
7. Use `set -euo pipefail` at the top

Output should look clean and readable.

[Click here for the script](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-18/script/system_info.sh)  

![system-info](https://github.com/itsme-sultan/90DaysOfDevOps/blob/master/2026/day-18/images/system_info.jpg)
---

