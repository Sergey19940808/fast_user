// This module for init mongodb store
db.createUser(
    {
        user: process.env.MONGO_USER,
        pwd: process.env.MONGO_PASSWORD,
        roles: [
            {
                role: process.env.MONGO_ROLE,
                db: process.env.MONGO_DATABASE
            }
        ]
    }
);