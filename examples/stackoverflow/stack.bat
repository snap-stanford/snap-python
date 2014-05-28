REM
REM	the script takes a file with StackOverflow posts,
REM	builds a graph of users posting questions and answers, and
REM	calculates some basic graph statistics
REM
REM     requirements:
REM       python installed
REM       Snap.py installed, http://snap.stanford.edu
REM       Posts.xml, https://archive.org/download/stackexchange/stackoverflow.com-Posts.7z, uncompress

echo ... "START analysis of StackOverflow"

REM get all the question posts and accepted answers (15min)
echo ... "extracting questions ..."
python getQuestions.py Posts.xml > questions.txt

REM get all the answer posts (15min)
echo ... "extracting answers ..."
python getAnswers.py Posts.xml > answers.txt

REM get all the Java question posts, id only (15min)
echo ... "identifying Java questions ..."
python getTag.py Posts.xml java > java.txt

REM select questions with a Java tag (20s)
echo ... "selecting Java questions ..."
python doJoin.py java.txt questions.txt 1 1 > java-posts.txt

REM identify users of accepted answers (40s)
echo ... "finding owners of accepted answers ..."
python doJoin.py answers.txt java-posts.txt 1 3 > qa.txt

REM create a graph and find top users (5s)
echo ... "building a QA graph and calculating statistics ..."
python getStats.py qa.txt 2 6

echo ... "END   analysis of StackOverflow"

