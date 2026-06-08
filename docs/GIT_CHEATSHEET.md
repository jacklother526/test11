# Git Cheat Sheet

## Basic Commands

### Clone a Repository
```bash
git clone https://github.com/username/repo.git
cd repo
```

### Check Status
```bash
git status              # See changed files
git diff                # See what changed
git log                 # See commit history
```

### Stage and Commit
```bash
git add .               # Stage all changes
git add file.py         # Stage specific file
git commit -m "Message" # Commit with message
```

### Push and Pull
```bash
git push origin main    # Push to GitHub
git pull origin main    # Get latest from GitHub
```

## Branch Commands

### Create and Switch Branches
```bash
git branch                      # List local branches
git branch -a                   # List all branches
git branch feature-name         # Create new branch
git checkout feature-name       # Switch to branch
git checkout -b feature-name    # Create and switch in one command
```

### Delete Branches
```bash
git branch -d feature-name      # Delete local branch
git push origin --delete feature-name  # Delete remote branch
```

## Merging

### Merge Branches
```bash
git checkout main               # Switch to main
git pull origin main            # Get latest main
git merge feature-name          # Merge feature into main
git push origin main            # Push merged code
```

## Undoing Changes

### Revert Changes
```bash
git checkout -- file.py         # Discard changes in file
git reset HEAD file.py          # Unstage file
git reset --soft HEAD~1         # Undo last commit (keep changes)
git reset --hard HEAD~1         # Undo last commit (discard changes)
git revert HEAD                 # Create new commit that undoes previous
```

## Advanced Commands

### Rebase (Advanced)
```bash
git rebase main                 # Rebase current branch onto main
git rebase --continue           # Continue after resolving conflicts
git rebase --abort              # Cancel rebase
```

### Stash (Temporarily Save Changes)
```bash
git stash                       # Save changes temporarily
git stash list                  # List stashed changes
git stash pop                   # Restore last stash
git stash apply stash@{0}       # Apply specific stash
```

### View History
```bash
git log --oneline               # Condensed commit history
git log -n 5                    # Show last 5 commits
git log --graph --all           # Visual branch history
git show commit-hash            # Show specific commit
```

## Useful Configurations

### Set Your Identity
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Create Aliases (Shortcuts)
```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
```

Now you can use:
```bash
git st      # instead of git status
git co      # instead of git checkout
```

## Common Workflows

### Feature Development Workflow
```bash
1. git checkout -b feature/new-feature      # Create feature branch
2. # Make changes
3. git add .
4. git commit -m "Add new feature"
5. git push origin feature/new-feature      # Push to GitHub
6. # Create Pull Request on GitHub
7. # After review and approval:
8. git checkout main
9. git pull origin main
10. git merge feature/new-feature
11. git push origin main
12. git branch -d feature/new-feature       # Clean up
```

### Sync Local with Remote
```bash
git fetch origin                # Get latest info
git status                      # See if behind
git pull origin main            # Update local main
```

### Fix Last Commit
```bash
# Made a typo in commit message?
git commit --amend -m "Corrected message"

# Forgot to add a file?
git add forgotten-file.py
git commit --amend
```

## Troubleshooting

### Merge Conflicts
```bash
# Conflicts occur when same lines are changed
# Edit the file to resolve conflicts
# Look for:
# <<<<<<< HEAD
# your changes
# =======
# incoming changes
# >>>>>>>

# After resolving:
git add .
git commit -m "Resolve merge conflict"
```

### Accidentally Pushed to Wrong Branch
```bash
# Don't panic! You can fix it:
git revert HEAD             # Create reverting commit
git push origin branch-name
```

## Tips

- **Commit Often**: Make small, logical commits
- **Write Good Messages**: Describe WHY, not just WHAT
- **Pull Before Push**: Avoid conflicts
- **Never Force Push to Main**: Only on personal branches
- **Use .gitignore**: Don't commit sensitive files
- **Review Before Committing**: `git diff` before `git add`
