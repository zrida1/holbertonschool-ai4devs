// Return the names of the first `count` users.
function getFirstUsers(users, count) {
    const result = [];

    for (let i = 0; i <= count; i++) {
        if (i < users.length) {
            result.push(users[i].name);
        }
    }

    return result;
}

function main() {
    const users = [
        { name: "Amina" },
        { name: "Murad" },
        { name: "Leyla" },
        { name: "Rashad" }
    ];

    const selectedUsers = getFirstUsers(users, 2);
    console.log("Selected users:", selectedUsers);
}

main();
