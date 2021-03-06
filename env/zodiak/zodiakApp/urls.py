from django.conf.urls import include, url
from django.conf import settings
from . import views

# from custom_functions import calculator,export_csv

urlpatterns = [
    url(r'^$', views.adminPage, name='adminPage'),
    # url(r'^$', views.homepage, name='homepage'),
    # url(r'^index/$', views.index, name='index'),

    url(r'^accounts/login/$', views.user_login, name="login"),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name="register"),
    url(r'^home/$', views.clientpage, name="clientpage"),
    url(r'^reporting/$', views.reporting, name="reporting"),

    url(r'^viewjobs/(?P<jobtype>.+)$', views.view_jobs, name="view_jobs"),
    url(r'^eidtOBJ/$', views.editOBJ, name="editOBJ"),
    url(r'^newFilter/$', views.new_filter, name="new_filter"),
    url(r'^myjobs/(?P<jobtype>.+)$', views.view_user_jobs, name="view_user_jobs"),
    url(r'^addjob/(?P<jobtype>.+)$', views.add_job, name="add_job"),
    url(r'^addjob4/(?P<jobtype>.+)$', views.add_job4, name="add_job4"),
    url(r'^jobedit/(?P<pk>.+)/$', views.job_edit, name="job_edit"),
    url(r'^jobview/(?P<pk>.+)/$', views.job_view, name="job_view"),
    url(r'^jobdelete/(?P<pk>.+)/$', views.job_delete, name="job_delete"),
    url(r'^jobprocess/(?P<pk>.+)/$', views.process_job, name="process_job"),
    url(r'^procjob/(?P<pk>.+)/$', views.process_spec_job, name="process_spec_job"),
    url(r'^editbatch/$', views.editbatch, name="editbatch"),
    url(r'^editContainer/$', views.editContainer, name="editContainer"),

    url(r'^useredit/(?P<pk>.+)/$', views.user_edit, name="user_edit"),
    url(r'^userview/(?P<pk>.+)/$', views.user_view, name="user_view"),
    url(r'^myprofile/(?P<username>.+)/$', views.user_view_home, name="user_view_home"),
    url(r'^userdelete/(?P<pk>.+)/$', views.user_delete, name="user_delete"),
    url(r'^viewusers/$', views.viewusers, name="viewusers"),
    url(r'^viewshippers/$', views.viewshippers, name="viewshippers"),
    url(r'^adduser/$', views.addUser, name="add_user"),

    url(r'^addbatch/$', views.add_batch, name="add_batch"),
    url(r'^viewbatches/$', views.viewbatches, name="viewbatches"),
    url(r'^batchedit/(?P<pk>.+)/$', views.batch_edit, name="batch_edit"),
    url(r'^batchprocess/(?P<pk>.+)/$', views.batch_process, name="batch_process"),
    url(r'^viewminibatches/(?P<pk>.+)/$', views.viewminibatches, name="viewminibatches"),
    url(r'^batchmanifest/(?P<pk>.+)/$', views.print_manifest, name="print_manifest"),

    url(r'^getDel/(?P<pk>.+)/(?P<identifier>.+)/$', views.get_del_item, name="get_del_item"),
    url(r'^batchdelete/(?P<pk>.+)/$', views.batch_delete, name="batch_delete"),
    url(r'^batch_info_view/(?P<pk>.+)/$', views.batch_info_view, name="batch_info_view"),
    url(r'^jobinvoice/(?P<pk>.+)/$', views.job_invoice_page, name="job_invoice_page"),

    url(r'^jobComments/$', views.get_job_comments, name="get_job_comments"),
    url(r'^jobdesc/$', views.get_job_desc, name="get_job_desc"),
    url(r'^jobinfo/$', views.get_job_info, name="get_job_info"),

    url(r'^jobfinancials/(?P<job_obj>.+)/$', views.financials, name="financials"),
    url(r'^financeRecords/$', views.financerecords, name="financerecords"),

    url(r'^docrecords/$', views.docrecords, name="docrecords"),
    url(r'^docedit/(?P<pk>.+)/$', views.new_doc_info_edit, name="new_doc_info_edit"),
    url(r'^docs/$', views.add_new_doc, name="add_new_doc"),
    url(r'^shipperAdd/$', views.add_new_shipper, name="add_new_shipper"),
    url(r'^shipperEdit/$', views.editshipper, name="editshipper"),
    url(r'^userAdd/$', views.add_new_user, name="add_new_user"),
    url(r'^statrecords/$', views.statrecords, name="statrecords"),
    url(r'^statedit/(?P<pk>.+)/$', views.new_stat_info_edit, name="new_stat_info_edit"),
    url(r'^statdelete/(?P<pk>.+)/$', views.stat_info_delete, name="stat_info_delete"),
    url(r'^newType/$', views.new_type, name="new_type"),
    url(r'^newStat/$', views.new_stat, name="new_stat"),

    url(r'^fin_info_view/(?P<pk>.+)/$', views.fin_info_view, name="fin_info_view"),
    url(r'^fin_info_edit/(?P<pk>.+)/$', views.fin_info_edit, name="fin_info_edit"),
    url(r'^fin_info_delete/(?P<pk>.+)/$', views.fin_info_delete, name="fin_info_delete"),
    url(r'^newFinance/$', views.new_financials, name="new_financials"),
    url(r'^newFinEdit/(?P<pk>.+)/$', views.new_fin_info_edit, name="new_fin_info_edit"),
    url(r'^newFinAdd/(?P<job_id>.+)/$', views.new_fin_info_add, name="new_fin_info_add"),

    url(r'^edit-access$', views.user_access, name="user_access"),
    url(r'^mailbox/$',views.mails, name = "mails"),
    url(r'^newmail/$',views.newmail, name = "newmail"),
    url(r'^viewmail/(?P<pk>.+)/$', views.view_mail, name="view_mail"),

    url(r'^jobdocs/(?P<job_obj>.+)/$', views.addDoc, name="addDoc"),
    url(r'^delete_doc/(?P<pk>.+)/$', views.delete_doc, name="delete_doc"),
    url(r'^delete_shipper/(?P<pk>.+)/$', views.delete_shipper, name="delete_shipper"),
    url(r'^processjob/(?P<job_obj>.+)$',views.process_job, name = "process_job"),

    url(r'^addrm/$',views.add_rm, name = "add_rm"),
    url(r'^viewrms/$',views.viewrms, name = "viewrms"),

    url(r'^postComments/(?P<pk>.+)/$',views.post_comments, name = "post_comments"),

    url(r'^rmedit/(?P<pk>.+)/$', views.rm_edit, name="rm_edit"),
    url(r'^rmview/(?P<pk>.+)/$', views.rm_view, name="rm_view"),
    url(r'^rmdelete/(?P<pk>.+)/$', views.rm_delete, name="rm_delete"),

    url(r'^quoteAdd/$',views.quote_add, name = "quote_add"),
    url(r'^viewquotations/$',views.viewquotations, name = "viewquotations"),

    url(r'^quoteedit/(?P<pk>.+)/$', views.quote_edit, name="quote_edit"),
    url(r'^quoteview/(?P<pk>.+)/$', views.quote_view, name="quote_view"),
    url(r'^quotedelete/(?P<pk>.+)/$', views.quote_delete, name="quote_delete"),
    url(r'^add_officeusecase/(?P<pk>.+)/$', views.add_officeusecase, name="add_officeusecase"),

    # url(r'^confirm-order/$',views.get_confirmation_order, name = "get_confirmation_order"),
    url(r'^getjob/$',views.get_job, name = "get_job"),
    url(r'^getUserDetails/$',views.get_user_details, name = "get_user_details"),
    url(r'^getShippersDetails/$',views.get_shippers_details, name = "get_shippers_details"),

    url(r'^selectedjobs/$',views.get_jobs_selected, name = "get_jobs_selected"),
    # url(r'^customer-list/$',views.all_customers, name = "all_customers"),
    # url(r'^customer-payment-list/$',views.customer_payments, name = "all_customers_payments"),
    # # url(r'^userComment/$',views.user_comment, name = "user_comment"),
    # # url(r'^search-results/(?P<action>[-\w]+)/$',views.user_search, name = "user_search"),
    # url(r'^remove-from-cart/(?P<item_pk>[-\w]+)/$',views.remove_from_cart, name = "remove_from_cart"),
    # url(r'cart-box/$',views.cart_box, name = "cart_box"),
    # url(r'^items/(?P<category>[-\w]+)/$',views.allStoreItems, name = "all-items"),
    # url(r'^getRecord/(?P<action>.+)/(?P<identifier>.+)/(?P<pk>.+)/$',views.get_record, name = "get_record"),
    # url(r'^viewService/(?P<identifier>.+)/(?P<pk>.+)/$',views.view_service, name = "view_service"),
    # url(r'^storeitems/(?P<category>[-\w]+)/(?P<subcategory>[-\w]+)/$',views.storeItems, name = "store-items"),
    # url(r'invoice/(?P<tracking_id>.+)/$', views.package_invoice_page, name="package_invoice"),
    # # url(r'^calculator/$', calculator, name ="calculator"),
    # # url(r'^export/csv/$', export_csv, name='export_csv'),
    # # url(r'^staff-login-access/$', views.staff_login_access, name="staff_login_access"),
    # url(r'^customer-orders/$', views.customer_orders, name="all_customer_orders"),
    # url(r'^packages/$', views.customer_packages, name="all_customer_packages"),
    # # url(r'^vendor/play/$', views.get_play_event, name="get_play_event"),
    # # url(r'^export/tradingDetails/(?P<useracc_obj>[-\w]+)/$', views.tradingDetails, name='tradingDetails'),
    # # url(r'^closing/djp/$', views.close_djp_client, name="close_djp_client"),
    # # pay-pal
    # url(r'^confirm_paypal_payment/$', views.confirm_paypal_payment, name="confirm_paypal_payment"),

]

