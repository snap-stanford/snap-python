#
#	the script takes a file with StackOverflow posts,
#	builds a graph of users posting questions and answers, and
#	calculates some basic graph statistics
#
#	requirements:
#	  python installed
#	  Snap.py installed, http://snap.stanford.edu
#	  Posts.xml, https://archive.org/download/stackexchange/stackoverflow.com-Posts.7z, uncompress

echo `date` ... "START analysis of StackOverflow"

# get all the question posts and accepted answers (15min)
echo `date` ... "extracting questions ..."
python getQuestions.py Posts.xml > questions.txt

# get all the answer posts (15min)
echo `date` ... "extracting answers ..."
python getAnswers.py Posts.xml > answers.txt

# get all the Java question posts, id only (15min)
echo `date` ... "identifying Java questions ..."
python getTag.py Posts.xml java > java.txt

# select questions with a Java tag (20s)
echo `date` ... "selecting Java questions ..."
python doJoin.py java.txt questions.txt 1 1 > java-posts.txt

# identify users of accepted answers (40s)
echo `date` ... "finding owners of accepted answers ..."
python doJoin.py answers.txt java-posts.txt 1 3 > qa.txt

# create a graph and find top users (5s)
echo `date` ... "building a QA graph and calculating statistics ..."
python getStats.py qa.txt 2 6

echo `date` ... "END   analysis of StackOverflow"

