document.addEventListener('DOMContentLoaded', function () {
    fetchContacts();
});

function fetchContacts() {
    fetch('/contacts')
        .then(response => response.json())
        .then(data => {
            const contactsList = document.getElementById('contacts');
            contactsList.innerHTML = '';
            data.forEach(contact => {
                const li = document.createElement('li');
                li.innerHTML = `${contact.name} - ${contact.phone} <button onclick="deleteContact(${contact.id})">Delete</button>`;
                contactsList.appendChild(li);
            });
        });
}

function addContact() {
    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;

    fetch('/contacts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, phone }),
    })
    .then(response => response.json())
    .then(() => {
        document.getElementById('name').value = '';
        document.getElementById('phone').value = '';
        fetchContacts();
    });
}

function deleteContact(contactId) {
    fetch(`/contacts/${contactId}`, {
        method: 'DELETE',
    })
    .then(() => {
        fetchContacts();
    });
}
