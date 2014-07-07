# !/bin/sh
# This script does a git check-out of all the dependent repositories of Seash to the home directory.
# <Usage>
# sh setup.sh
# <Example>
# Clone the seash repository to local machine, and run this script
# seash user$ sh setup.sh

REPO_1=`curl https://api.github.com/orgs/SeattleTestbed/repos | awk '/ *\"seattlelib_v2\",/ {print $2}' | tr -d \",`
REPO_2=`curl https://api.github.com/orgs/SeattleTestbed/repos | awk '/ *\"clearinghouse\",/ {print $2}' | tr -d \",`
REPO_3=`curl https://api.github.com/orgs/SeattleTestbed/repos | awk '/ *\"portability\",/ {print $2}' | tr -d \",`
REPO_4=`curl https://api.github.com/orgs/SeattleTestbed/repos | awk '/ *\"repy_v2\",/ {print $2}' | tr -d \",`
REPO_5=`curl https://api.github.com/orgs/SeattleTestbed/repos | awk '/ *\"repy_v1\",/ {print $2}' | tr -d \",`
REPO_6=`curl https://api.github.com/orgs/SeattleTestbed/repos | awk '/ *\"dist\",/ {print $2}' | tr -d \",`

for REPO in $REPO_1 ;
  do git clone https://github.com/SeattleTestbed/$REPO.git ;
done

for REPO in $REPO_2 ;
  do git clone https://github.com/SeattleTestbed/$REPO.git ;
done

for REPO in $REPO_3 ;
  do git clone https://github.com/SeattleTestbed/$REPO.git ;
done

for REPO in $REPO_4 ;
  do git clone https://github.com/SeattleTestbed/$REPO.git ;
done

for REPO in $REPO_5 ;
  do git clone https://github.com/SeattleTestbed/$REPO.git ;
done

for REPO in $REPO_6 ;
  do git clone https://github.com/SeattleTestbed/$REPO.git -b git-aware-buildscripts ;
done