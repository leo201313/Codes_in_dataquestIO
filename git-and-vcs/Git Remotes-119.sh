## 1. Introduction to Remote Repositories ##

/home/dq$ git clone /dataquest/user/git/chatbot chatbot

## 2. Making Changes to Cloned Repositories ##

/home/dq/chatbot$ git commit -m 'Updated README.md'

## 3. Overview of the Master Branch ##

/home/dq/chatbot$ git branch

## 4. Pushing Changes to the Remote ##

/home/dq/chatbot$ git push origin master

## 5. Viewing Individual Commits ##

/home/dq/chatbot$ git show 8a74590e546a504c8a658958a2514de71c90bbe7

## 6. Commits and the Working Directory ##

/home/dq/chatbot$ git diff 8a74 d947

## 7. Switching to a Specific Commit ##

/home/dq/chatbot$ git reset --hard d947

## 8. Pulling From a Remote Repo ##

/home/dq/chatbot$ git pull

## 9. Referring to the Most Recent Commit ##

/home/dq/chatbot$ git reset --hard HEAD~1