
const appendDate = () => {
    targetForm = document.getElementById("AnswerForm");
    artificialInput = document.createElement("input");

    artificialInput.hidden = "true";
    artificialInput.type = "date";
    artificialInput.name = "date";
    artificialInput.valueAsDate = new Date();

    targetForm.appendChild(artificialInput);
};
