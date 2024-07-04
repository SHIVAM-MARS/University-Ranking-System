// script.js
document.getElementById('ranking-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const data = {
        InstituteName: document.getElementById('institute-name').value,
        TeachingLearningResources: parseInt(document.getElementById('teaching-learning-resources').value),
        ResearchProfessionalPractice: parseInt(document.getElementById('research-professional-practice').value),
        PlacementRecord: parseInt(document.getElementById('placement-record').value),
        OutreachInclusivity: parseInt(document.getElementById('outreach-inclusivity').value),
        Perception: parseInt(document.getElementById('perception').value),
    };
    console.log(data);

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: data,
    })
    .then(
        response => response.json(),
        console.log(response)
)
    .then(data => {
        const rank = data.rank;
        const fullData = data.data;
        console.log(rank);
        console.log(data);

        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td>${rank}</td>
            <td>${fullData.instituteName}</td>
            <td>${fullData.teachingLearningResources}</td>
            <td>${fullData.researchProfessionalPractice}</td>
            <td>${fullData.placementRecord}</td>
            <td>${fullData.outreachInclusivity}</td>
            <td>${fullData.perception}</td>
        `;

        document.querySelector('#ranking-table tbody').appendChild(newRow);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
