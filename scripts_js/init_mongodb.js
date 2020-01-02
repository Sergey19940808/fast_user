// This module for init mongodb store
db.createUser(
    {
        user: "fast_user",
        pwd: "vwD7ytjbFhH89t9F",
        roles: [
            {
                role: "readWrite",
                db: "fast_user"
            }
        ]
    }
);