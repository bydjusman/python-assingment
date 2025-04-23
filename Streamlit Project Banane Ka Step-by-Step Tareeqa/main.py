# project deleted ho gaya hai laptop se no tension clone kro apni repo me jao

# Check karo Git connected hai:
git remote -v 

# Output kuch aisa hona chahiye:

origin  https://github.com/username/repo-name.git (fetch)
origin  https://github.com/username/repo-name.git (push)

# Agar ye hai toh perfect, warna remote add karna padega:

git remote add origin https://github.com/username/repo-name.git

git status 
git add .

# Agar tumne file delete/add ki:
git commit -m "Removed unused files" 
git commit -m "Added About page component"

git push -u origin main




