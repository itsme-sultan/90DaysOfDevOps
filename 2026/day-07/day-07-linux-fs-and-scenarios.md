# Linux File System Hierarchy & Scenario-Based Practice  

**Core Directories (Must Know):**
- `/` (root) - The starting point of everything. Every other directory branches off from there. I would use this to get into ;inux root system.
  
- `/home` - User home directories. Where your personal stuff lives, in a folder named after you: `/home/yourname.` . I would use this to list down all the user's home directory.
  
- `/root` - Root user's home directory. The home directory for the root (admin) user — not to be confused with /, the root of the whole tree.  I would use this to store files that only root should acsess.
  
- `/etc` - Configuration files. Almost every program stores its settings here as plain text (e.g. /etc/passwd, /etc/hosts). I would this to customize 
  
- `/var/log` - Log files.  where Linux keeps its logs — records of what the system, kernel, and various services have been doing. If something breaks, this is usually the first place to look.  
   `auth.log` : I would use this to check logs related to authentication.  
   `syslog` : I would use this tview general system and service related logs.
  
- `/tmp` - Temporary files. Scratch space for temporary files. Often wiped on reboot. I would use this to store temporary file.

**Additional Directories (Good to Know):**
- `/bin` - Essential command binaries.  held commands essential for basic system operation, needed even before other filesystems (like /usr) were mounted. Things like ls, cp, mv, cat, bash.
  
- `/usr/bin` - Contains the majority of user command binaries — programs and utilities that regular users and administrators run in daily work. (ex. ls, mkdir, mv) I would use this to look for commands.
  
- `/opt` - Optional third-party software that doesn't follow the standard packaging conventions.
