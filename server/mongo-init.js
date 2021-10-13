db.createUser(
    {
        user: "root",
        pwd: "toor",
        roles: [
            {
                role: "readWrite",
                db: "lost_in_paradise"
            }
        ]
    }
);