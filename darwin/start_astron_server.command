cd `dirname $0`
cd ..
cd astron

wine ./astrond --loglevel info config/astrond.yml
