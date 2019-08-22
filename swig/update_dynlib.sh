#
#	The script updates the dynamic library in _snap.so
#	for a non-system Python, such as Anaconda or Homebrew
#
#	Usage:
#		update_dynlib.sh <dylib_path>
#

ORIG_PATH=/System/Library/Frameworks/Python.framework/Versions/2.7/Python
if [ "$2" = "3" ]; then
	ORIG_PATH=/usr/local/opt/python/Frameworks/Python.framework/Versions/3.7/Python
fi

LIB_NAME=_snap.so
BACKUP_NAME=_snap-bak.so

# test for a non-empty parameter
if test -z "$1"; then
	echo "*** Usage: update_dynlib.sh <dylib_path>"
	exit 42
fi

NEW_PATH=$1

if [ "$ORIG_PATH" = "$NEW_PATH" ]; then
	echo "exiting, the new path is the same as the current one" $ORIG_PATH  $NEW_PATH
	exit 0
fi

# create a backup copy, if it does not yet exist
if [ ! -f $BACKUP_NAME ]; then
	echo "creating a backup copy" $BACKUP_NAME "..."
	cp -a $LIB_NAME $BACKUP_NAME
fi

# take a fresh copy from backup
echo "getting a new copy of" $LIB_NAME "from" $BACKUP_NAME "..."
cp -a $BACKUP_NAME $LIB_NAME

# change the Python library path
echo "current Python library path is" $ORIG_PATH
echo "changing the Python library path to" $NEW_PATH "..."
./install_name_tool -change $ORIG_PATH $NEW_PATH $LIB_NAME

exit 0

