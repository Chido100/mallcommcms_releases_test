__author__ = 'Chidozie Amefule'


class Locator(object):
    # Login page
    login_email = "//div[@class='login-container']//input[@id='username']"
    login_next_button = "//div[@class='login-container']//button"
    login_with_toolbox = "//span[@class='col-span-8']"
    choose_account = "//div[@class='WBW9sf']//div[contains(text(),'Chidozie Amefule')]"
    select_database = "//div[@class='container p30']//div[26]//button"
    print_email = "//div[@class='aCsJod oJeWuf']//input[@id='identifierId']"
    print_email_next_button = "//div[@class='F9NWFb']//span[@class='VfPpkd-vQzf8d']"
    print_password = "//div[@id='password']//input"
    print_password_next_button = "//div[@class='F9NWFb']//span[@class='VfPpkd-vQzf8d']"

    # Switch centre
    switch_centre = "//div[@class='pull-right']//button[contains(text(), 'Switch centre')]"
    test_centre = "//div[@class='modal-body']//div[contains(text(), 'QA Release Environment')]"
    switch_centre_button = "//div[@class='modal-footer']//button[contains(text(), 'Switch centre')]"

    # Stores
    stores_dropdown = "//div[@class='container']//li[2]"

    """ -----All Stores----- """
    all_stores = "//div[@class='container']//li[2]//ul[@class='dropdown-menu']//span[contains(text(),'All Stores')]"
    edit_store_button = "//div[@class='table-responsive']//tr[@class='odd']//td[1]"
    update_store_button = "//div[@class='pull-right']//button[contains(text(), 'Update')]"
    check_all_stores = "//div[@class='alert alert-success']"

    """ -----Add Store----- """
    add_new_store = "//div[@class='container']//li[2]//ul[@class='dropdown-menu']//span[contains(text(),'Add new')]"
    select_store_name_dropdown = "//span[@class='selection']//span[contains(text(), 'Select')]"
    store_selected = "//li[contains(text(), 'M&S Cafe')]"
    estimated_number_of_staff_input = "//div[@class='tab-content']//input[@id='staff_num']"
    create_store_button = "//div[@class='pull-right']//button[contains(text(), 'Create store')]"
    success = "//div[@class='col-xs-12']//div[contains(text(), 'Your store has been')]"

    # People
    people_dropdown = "//li[3][@class='dropdown']"

    """ -----All People----- """
    all_people = "//li[3][@class='dropdown open']//ul//li//span[contains(text(),'All People')]"
    check_all_people = "//div[@class='pull-left']//h3[contains(text(), 'All People')]"

    """ -----Add People----- """
    add_new_people = "//li[3][@class='dropdown open']//li//span[contains(text(),'Add new')]"
    first_name = "//input[@id='first_name']"
    last_name = "//input[@id='last_name']"
    add_people_email = "//input[@id='email']"
    password = "//input[@id='password']"
    confirm_password = "//input[@id='password_confirmation']"
    select_store_dropdown = "//span[contains(text(), 'Select store')]"
    add_people_store_selected = "//li[contains(text(), 'Mallcomm Team')][1]"
    select_role_dropdown = "//span[contains(text(), 'Select role')]"
    selected_role = "//li[contains(text(), 'Staff')][1]"
    create_button = "//input[@type='submit']"

    # CRM
    crm = "//li[3][@class='dropdown open']//li//span[contains(text(),'CRM')]"
    crm_page = "//div[@class='pull-left']//h3[contains(text(), 'CRM')]"

    # Awards
    awards = "//li[3][@class='dropdown open']//li//span[contains(text(),'Awards')]"
    check_awards = "//div[@class='row mt30']//label[contains(text(), 'Given by')]"

    # Virtual Onboarding
    virtual_onboarding = "//li[3][@class='dropdown open']//li//span[contains(text(),'Virtual Onboarding')]"
    import_contacts = "//div[@class='row']//a[contains(text(), 'Import Contacts')]"

    # Items
    items_dropdown = "//li[4][@class='dropdown']"
    # All Items
    all_items = "//li[4][@class='dropdown open']//li//span[contains(text(),'All items')]"
    check_page = "//div[@class='col-xs-12 col-sm-4']//h3"
    # Add Item
    add_new_item = "//li[4][@class='dropdown open']//li//span[contains(text(),'Add new item')]"
    item_title = "//div[@class='row']//input[@id='title']"
    save_continue_button = "//button[@name='create']"
    item_message = ""

    # Critical Comms
    critical_comms = "//li[4][@class='dropdown open']//li//a[contains(text(),'Critical Comms')]"

    # Mallcomm Mail
    mallcomm_mail = "//li[4][@class='dropdown open']//li//span[contains(text(),'Mallcomm mail')]"

    # Ticketing
    ticketing_dropdown = "//li[5][@class='dropdown']//span[contains(text(),'Ticketing')]"
    # All Tickets
    all_tickets = "//li[5][@class='dropdown open']//ul//span[contains(text(),'All tickets')]"
    check_all_ticket = "//div[@class='container']//h3[contains(text(), 'Performance')]"
    # Add Ticket
    add_new_ticket = "//li[5][@class='dropdown open']//ul//span[contains(text(),'Add new')]"
    select_category_dropdown = "//span[@class='selection']//span[contains(text(), 'Select category')]"
    selected_category = "//span[@class='select2-results']//li[contains(text(), 'Standard')]"
    select_a_person_dropdown = "//span[@class='selection']//span[contains(text(), 'Select person')]"
    selected_person = "//span[@class='select2-results']//li[contains(text(), 'Joe Bloggs')]"
    assign_store_to_ticket_dropdown = "//span[@class='selection']//span[contains(text(), 'Select store')]"
    selected_store = "//span[@class='select2-results']//li[contains(text(), 'Mallcomm Team')][2]"
    submit_add_ticket_button = "//input[@id='addTicketFormButton']"
    add_ticket_next_page = "//div[@class='mb15']//h3[contains(text(), 'Ticket Requester ')]"
    ticket_title = "//input[@name='title']"
    company = "//input[@name='company']"
    ticket_creator_name_field = "//input[@name='responsable']"
    ticket_details = "//textarea[@name='action']"
    ticket_end_date = "//input[@name='enddate']"
    selected_end_date = "//div[@class='calendar-table']//td[contains(text(), '16')]"
    date_apply = "//button[@class='applyBtn btn btn-sm btn-success']"
    place_of_work = "//input[@name='place_of_action']"
    ticket_add_button = "//input[@name='add']"

    # Manage
    manage_dropdown = "//li[8][@class='dropdown']"
    # CMS Users
    cms_users_dropdown = "//ul[@class='dropdown-menu']//a[contains(text(), 'CMS users')]"
    all_cms_users = "//ul[@class='dropdown-menu']//span[contains(text(), 'All CMS users')]"
    add_cms_user_button = "//div[@class='pull-right']//button[contains(text(), 'Add CMS user')][1]"
    add_cms_first_name = "//div[@id='addCmsUser']//input[@name='firstname']"
    add_cms_last_name = "//div[@id='addCmsUser']//input[@name='lastname']"
    add_cms_email = "//div[@id='addCmsUser']//input[@name='email']"
    add_cms_role_toggle = "//div[@class='material-switch pull-right']//input[@id='basic']"
    add_cms_user_create_button = "//div[@id='addCmsUser']//button[contains(text(), 'Add CMS user')]"
    add_cms_user_success = "//div[@class='alert alert-success']"
    # CMS User Roles
    cms_user_roles = ""

    # Your Centre
    your_centre_dropdown = "//ul[@class='dropdown-menu']//a[contains(text(), 'Your centre')]"
    manage_your_buttons = "//ul[@class='dropdown-menu']//span[contains(text(), 'Manage your buttons')]"
    add_new_button = "//a[@class='btn btn-default']"
    button_name = "//div[@class='input-group']//input[@name='name']"
    create_button_button = "//input[@name='add-button']"


    # System Config
    system_config_dropdown = "//ul[@class='dropdown-menu']//a[contains(text(), 'System config')]"
    centre_config = "//ul[@class='dropdown-menu']//li[@class='dropdown-submenu']//span[contains(text(), 'Centre config')]"

    # Ticket Permissions
    ticket_permissions = "//ul[@class='dropdown-menu']//span[contains(text(), 'Ticket permissions')]"
    # Ticket Notifications
    ticket_notifications = "//ul[@class='dropdown-menu']//span[contains(text(), 'Ticket notifications')]"
    # Ticket Responses
    ticket_responses = "//ul[@class='dropdown-menu']//span[contains(text(), 'Ticket responses')]"
    # Ticket Reassign Statuses
    ticket_reassign_statuses = "//ul[@class='dropdown-menu']//span[contains(text(), 'Ticket reassign statuses')]"
    # Form Builder
    form_builder = "//ul[@class='dropdown-menu']//span[contains(text(), 'Form Builder')]"
    # Policies
    policies = "//ul[@class='dropdown-menu']//span[contains(text(), 'Policies')]"
    # CMS Notification Centre
    cms_notification_centre = "//ul[@class='dropdown-menu']//span[contains(text(), 'CMS Notification centre')]"
    # Add Centre
    add_centre = "//ul[@class='dropdown-menu']//span[contains(text(), 'Add centre')]"
    centre_name = "//div[@class='container']//input[@id='name']"
    centre_owner_dropdown_button = "//div[@class='form-group']//span[contains(text(), 'No owner')]"
    centre_owner_dropdown = "//span[@class='select2-results']//li[contains(text(), 'Toolbox Group')]"
    phone_code_dropdown_button = "//div[@class='form-group']//span[contains(text(), 'Select phone')]"
    phone_code_dropdown = "//span[@class='select2-results']//li[contains(text(), 'UK')]"
    add_centre_language_dropdown_button = "//div[@class='form-group']//span[contains(text(), 'Select centre language')]"
    add_centre_language_dropdown = "//span[@class='select2-results']//li[contains(text(), 'English')]"
    add_centre_app_button = "//div[@class='form-group']//span[contains(text(), 'App not')]"
    add_centre_app = "//span[@class='select2-results']//li[contains(text(), 'Mallcomm Plus')]"
    add_centre_create_button = "//div[@class='pull-right']//button[contains(text(), 'Create Centre')]"

    # Clone Centre
    clone_centre = "//ul[@class='dropdown-menu']//span[contains(text(), 'Clone centre')]"
    select_a_centre = "//div[@class='form-group']//span[contains(text(), 'Select a centre')]"
    selected_centre_to_clone = "//span[@class='select2-results']//li[contains(text(), 'Chido Centre ')]"
    choose_file_button = "//input[@name='main_logo']"
    new_centre_name = "//div[@class='form-group']//input[@class='form-control']"
    multi_clone_button = "//div[@class='col-xs-12']//span[@class='glyphicon glyphicon-plus pointer text-info f20 duplicate']"
    create_clone_button = "//div[@class='pull-right']//button[@id='clone_centre']"
    agreement_modal = "//div[@class='modal-content']//button[contains(text(), 'I agree')]"
    clone_complete = "//h2[@class='swal2-title']"
    clone_centre_plus_sign = "//span[@class='glyphicon glyphicon-plus pointer text-info f20 duplicate']"


    # Templates
    templates = "//ul[@class='dropdown-menu']//li//a[contains(text(), 'Templates')]"
    add_new_template_button = "//div[@class='pull-right']//i"
    template_name = "//div[@class='form-group']//input[@id='name']"
    template_display_name = "//div[@class='form-group']//input[@id='displayname']"
    template_data = "//div[@class='form-group']//div//p"
    template_save_button = "//div[@class='form-group']//button[contains(text(), 'Save')]"



    

    # Remove Centre API Keys
    remove_centre_api_keys = "//ul[@class='dropdown-menu']//span[contains(text(), 'Remove Centre API Keys')]"

    # Ticketing approval flows
