var fieldId = 0; // used by the addField() function to keep track of IDs
function addField() {
    fieldId++;
    var newField = document.getElementById('newField');
    var html = '<input type="text" placeholder=\'' + newField.value + '\' /> ' +
               '<input type="button" value="-" onclick="removeEl(\'field-' + fieldId + '\');"/>';
    addEl('fields', 'p', 'field-' + fieldId, html);
}

// Add new element to the form
function addEl(parentId, elementTag, elementId, html) {
    var p = document.getElementById(parentId);
    var newElement = document.createElement(elementTag);
    newElement.setAttribute('id', elementId);
    newElement.innerHTML = html;
    p.appendChild(newElement);
}

// Remove exist element from form
function removeEl(elementId) {
    var element = document.getElementById(elementId);
    element.parentNode.removeChild(element);
}