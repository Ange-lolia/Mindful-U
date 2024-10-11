// resources.js

document.addEventListener('DOMContentLoaded', function () {
    console.log('Resources page loaded');

    const resourcesSection = document.getElementById('resources-section');
    const resources = [
        { name: "Mental Health America", link: "https://www.mhanational.org/" },
        { name: "National Alliance on Mental Illness (NAMI)", link: "https://www.nami.org/Home" },
        { name: "Headspace", link: "https://www.headspace.com/" }
    ];

    resources.forEach(resource => {
        const resourceItem = document.createElement('li');
        const resourceLink = document.createElement('a');
        resourceLink.href = resource.link;
        resourceLink.textContent = resource.name;
        resourceLink.target = "_blank";
        resourceItem.appendChild(resourceLink);
        resourcesSection.appendChild(resourceItem);
    });
});
