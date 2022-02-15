odoo.define ('newmodule_hr_timesheet_sheet.sheet', function (require) {
"use strict";
var DocumentsKanbanController = require('documents.DocumentsKanbanController');
var DocumentsKanbanModel = require('documents.DocumentsKanbanModel');
var DocumentsKanbanRenderer = require('documents.DocumentsKanbanRenderer');
var DocumentsSearchPanel = require('documents.DocumentsSearchPanel');

var core = require('web.core');
var KanbanView = require('web.KanbanView');
var view_registry = require('web.view_registry');
var documentss= require('documents.DocumentsKanbanController')


    setInterval(function(){
    var sessionss = require ('web.session');
    sessionss.user_has_group('custom.group_document_view'). then (function (has_group) {

    if (has_group) {
        $(".o_documents_kanban_upload").hide();
        $(".o_documents_kanban_url").hide();
    }
    }, 300);

});
});





