#!/bin/bash

# ensure that cwd is project root
cd $(dirname $0)

current_hash=$(cat sync-cursor)

git fetch upstream develop
# crop to 7 chars
next_hash=$(git rev-parse upstream/develop)
next_hash=${next_hash:0:7}

if [ ${current_hash} == ${next_hash} ]; then
  exit 0
fi

# for every commit in the range, create a patch file
for commit in $(git rev-list ${current_hash}..${next_hash}); do
  commit=$(echo ${commit} | cut -c1-7)
  git diff ${commit}^ ${commit} > ${commit}.patch
done

echo ${next_hash} > sync-cursor
