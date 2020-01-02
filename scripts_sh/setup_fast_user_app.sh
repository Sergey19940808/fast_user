# Setup env for functionality of api
DIR_LOGS='logs'
if [ ! -d $DIR_LOGS ]; then
    mkdir $DIR_LOGS
fi

# Setup env for functionality of db
DIR_MONGO_DB='mongo-db'
if [ ! -d $DIR_MONGO_DB ]; then
    mkdir $DIR_MONGO_DB
fi