document.addEventListener("DOMContentLoaded", function () {

    function createNewField(containerId, formHtml) {
        let container = document.getElementById(containerId);
        let newField = document.createElement("div");
        newField.innerHTML = formHtml;
        container.appendChild(newField);
    }

    window.addEducation = function () {
        createNewField("education-container", `{{ education_form.as_p|safe }}`);
    };

    window.addProject = function () {
        createNewField("project-container", `{{ project_form.as_p|safe }}`);
    };

    window.addPublication = function () {
        createNewField("publication-container", `{{ publication_form.as_p|safe }}`);
    };

    window.addCertification = function () {
        createNewField("certification-container", `{{ certification_form.as_p|safe }}`);
    };

    window.addAchievement = function () {
        createNewField("achievement-container", `{{ achievement_form.as_p|safe }}`);
    };

    window.addSkill = function () {
        createNewField("skill-container", `{{ skill_form.as_p|safe }}`);
    };
});
