# GitHub Workflow Examples

This guide shows you practical examples of common GitHub workflows.

## 1. Creating and Managing Branches

### Creating a Feature Branch
```bash
# Create and switch to a new branch
git checkout -b feature/user-authentication

# Make your changes
echo "New feature code" >> src/auth.py

# Stage and commit
git add src/auth.py
git commit -m "Add user authentication module"

# Push to GitHub
git push origin feature/user-authentication
```

### Deleting a Branch (After Merging)
```bash
# Delete local branch
git branch -d feature/user-authentication

# Delete remote branch
git push origin --delete feature/user-authentication
```

## 2. Pull Request (PR) Workflow

### Step 1: Create Feature Branch
```bash
git checkout -b feature/add-database-support
```

### Step 2: Make Changes
```bash
# Edit files
# Commit changes
git add .
git commit -m "Add database connection module"
git push origin feature/add-database-support
```

### Step 3: Create Pull Request on GitHub
- Go to your repository on GitHub
- Click "Compare & pull request"
- Add title: "Add database support"
- Add description explaining what the PR does
- Click "Create pull request"

### Step 4: Review Process
- Reviewers check your code
- Discuss changes if needed
- Make requested changes by committing to the same branch
- Automatically updates the PR

### Step 5: Merge
- Click "Merge pull request"
- Delete the branch

## 3. Common Git Commands

### Checking Status
```bash
# See what files have changed
git status

# See what changes you made
git diff
```

### Working with Commits
```bash
# View commit history
git log

# View last 5 commits
git log -5

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1
```

### Syncing with Main
```bash
# Update your main branch from remote
git checkout main
git pull origin main

# Update your feature branch with latest main
git checkout feature/my-feature
git rebase main
```

## 4. Collaborative Example

### Scenario: You and a Team Member Working Together

**You:**
```bash
# You create a feature
git checkout -b feature/api-endpoint
echo "@app.route('/api/users')" >> src/api.py
git add .
git commit -m "Add users API endpoint"
git push origin feature/api-endpoint
```

**On GitHub:**
- Create Pull Request
- Add description: "Adds GET /api/users endpoint"

**Team Member Reviews:**
- Sees your PR
- Comments: "Need error handling"

**You Update:**
```bash
# Still on feature/api-endpoint
echo "try-except block" >> src/api.py
git add .
git commit -m "Add error handling to API endpoint"
git push origin feature/api-endpoint
```

**Automatic Update:**
- PR automatically updates with your new commit
- Team member sees the change

**Team Member Approves and Merges**

## 5. Issues and Bug Tracking

### Creating an Issue on GitHub
```
Title: "Fix: Login button not working on mobile"
Description:
## Problem
The login button doesn't respond to taps on mobile devices.

## Steps to Reproduce
1. Go to login page
2. On mobile/tablet, tap the login button
3. Nothing happens

## Expected Behavior
Button should submit the login form

## Environment
- Browser: Chrome mobile
- Device: iPhone 12
- OS: iOS 16
```

### Linking PR to Issue
In your PR description, add:
```
Closes #42
```
When your PR merges, issue #42 automatically closes!

## 6. Commit Message Best Practices

### Good Commit Messages
```bash
# Clear and descriptive
git commit -m "Add email validation to signup form"

# With more details
git commit -m "Add email validation to signup form

- Validates email format
- Shows error message if invalid
- Prevents form submission until valid"
```

### Bad Commit Messages
```bash
git commit -m "update stuff"        # Too vague
git commit -m "fix bug"             # Unclear which bug
git commit -m "asdfghjkl"           # Meaningless
```

## 7. Real-World Workflow Summary

```
1. Clone repository
   git clone https://github.com/username/project.git

2. Create feature branch
   git checkout -b feature/my-feature

3. Make changes and commit
   git add .
   git commit -m "Descriptive message"

4. Push to GitHub
   git push origin feature/my-feature

5. Create Pull Request on GitHub
   - Describe what you changed and why
   - Link to related issues if any

6. Wait for review
   - Team reviews your code
   - Discuss any changes needed

7. Make requested changes
   git add .
   git commit -m "Address review feedback"
   git push origin feature/my-feature

8. Merge when approved
   - On GitHub, click Merge
   - Delete feature branch

9. Sync your local main
   git checkout main
   git pull origin main
```

## 8. Useful GitHub Features

### Labels
- **bug** - Something isn't working
- **enhancement** - New feature request
- **documentation** - Improvements or additions to documentation
- **good first issue** - Good for newcomers
- **help wanted** - Extra attention needed

### Milestones
- Group related issues/PRs
- Track progress toward a release

### Projects
- Kanban board for organizing work
- Columns: To Do, In Progress, Done

### Code Review
- Request reviewers before merging
- Discuss changes in comments
- Suggest specific code changes

## Resources

- [GitHub Docs](https://docs.github.com)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
