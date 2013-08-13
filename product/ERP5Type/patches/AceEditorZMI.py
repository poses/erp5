from App.Management import Navigation
from Acquisition import aq_parent

def manage_page_footer(self):
  default = '</body></html>'
  # Not within an ERP5 Site, use default footer
  if getattr(self, 'getPortalObject', None) is None:
    return default

  portal = self.getPortalObject()
  if portal.portal_preferences.getPreference('preferred_source_code_editor') != 'ace':
    return default

  # REQUEST['PUBLISHED'] can be the form in the acquisition context of the
  # document, or a method bound to the document (after a POST it is a bound method)
  published = self.REQUEST['PUBLISHED']
  document = getattr(published, 'im_self', None) # bound mehtod
  if document is None:
    document = aq_parent(published)

  if getattr(document, 'meta_type', None) is None:
    return default

  portal_url = portal.portal_url()
  mode = 'plain_text'    # default mode
  textarea_selector = '' # jQuery selector for the origin textarea that we will
                         # change into an ace editor

  if document.meta_type in ('DTML Document', 'DTML Method'):
    if document.getId().endswith('.js'):
      mode = 'javascript'
    elif document.getId().endswith('.css'):
      mode = 'css'
    textarea_selector = 'textarea[name="data:text"]'
  elif document.meta_type in ('File', ):
    if 'javascript' in document.getContentType():
      mode = 'javascript'
    elif 'css' in document.getContentType():
      mode = 'css'
    textarea_selector = 'textarea[name="filedata:text"]'
  elif document.meta_type in ('Script (Python)', ):
    mode = 'python'
    textarea_selector = 'textarea[name="body:text"]'
  elif document.meta_type in ('Z SQL Method', ):
    mode = 'sql'
    textarea_selector = 'textarea[name="template:text"]'
  elif document.meta_type in ('Page Template', 'ERP5 OOo Template', ):
    if 'html' in document.content_type:
      mode = 'html'
    else:
      mode = 'xml'
    textarea_selector = 'textarea[name="text:text"]'

  if not textarea_selector:
    return default
  return '''
<script type="text/javascript" src="%(portal_url)s/jquery/core/jquery.min.js"></script>
<script type="text/javascript" src="%(portal_url)s/ace/ace.js"></script>
<script type="text/javascript" src="%(portal_url)s/ace/mode-%(mode)s.js"></script>
<script type="text/javascript" src="%(portal_url)s/ace/ext-settings_menu.js"></script>

<script type="text/javascript">
$(document).ready(function() {
  var textarea = $('%(textarea_selector)s');
  if (textarea.length) {
    $('<div id="editor">')
      .css({"position": "relative", "height": textarea.height()})
      .appendTo(textarea.parent());
    textarea.hide();

    var editor = ace.edit("editor");

    var Mode = ace.require('ace/mode/%(mode)s').Mode;
    editor.getSession().setMode(new Mode());

    editor.getSession().setTabSize(2);

    editor.getSession().setValue(textarea.val());
    editor.getSession().on('change', function(){
      textarea.val(editor.getSession().getValue());
    });

    editor.commands.addCommand({
      name: "save",
      bindKey: {win: "Ctrl-S", mac: "Command-S"},
      exec: function() {
        $('input[value="Save Changes"]').click();
      }
    });

    ace.require('ace/ext/settings_menu').init(editor);
    editor.commands.addCommands([{
        name: 'showSettingsMenu',
        bindKey: {win: 'Alt-p', mac: 'Alt-p'},
        exec: function(editor) { editor.showSettingsMenu(); },
        readOnly: true
    }]);
  };
});
</script>
</body>
</html>''' % locals()

Navigation.manage_page_footer = manage_page_footer
