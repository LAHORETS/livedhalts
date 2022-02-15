
{
  "name"                 :  "Income Tax On Invoices And Bills",
  "summary"              :  """Income Tax on invoice/bill lines and invoices/bills along with fixed and percentage Income Tax""",
  "category"             :  "Accounting",
  "version"              :  "1.1.1",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "description"          :  """Odoo Income Tax On Bills""",
  "depends"              :  ['account'],
  "data"                 :  [
                             'security/security.xml',
                             'views/res_config_settings_view.xml',
                             'views/account_move_view.xml',
                             'report/report_invoice.xml',
                            ],
  "demo"                 :  ['data/discount_demo.xml'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
}
