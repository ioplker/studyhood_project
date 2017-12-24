using LiteDB;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Studyhood.client
{
    public partial class ViewNotifyForm : Form
    {
        private List<String> Notifications;

        public ViewNotifyForm()
        {
            InitializeComponent();

            this.Notifications = new List<String>();

            this.get_notifications();
        }

        private void get_notifications()
        {
            using (var DB = new LiteDatabase(@"StudyhoodData.db"))
            {
                var note_col = DB.GetCollection<server.Notify>("notifications");
                var note_cont = note_col.Find(x => x.Department == Department_Combo.Text);

                this.Notifications.Clear();
                Content_Text.Clear();
                Number_Combo.Items.Clear();
                int i = 0;
                foreach (server.Notify note in note_cont)
                {
                    i++;
                    this.Notifications.Add(note.Content);
                    Number_Combo.Items.Add(i);
                }
                if (i > 0)
                    Number_Combo.Text = "1";
                else
                    Number_Combo.Text = "-";

                note_col.EnsureIndex(x => x.Id);
            }

            this.update_content();
        }

        private void update_content()
        {
            if (Number_Combo.Text != "-")
                Content_Text.Text = this.Notifications[Convert.ToInt32(Number_Combo.Text)-1];
        }

        private void Number_Combo_SelectedIndexChanged(object sender, EventArgs e)
        {
            this.update_content();
        }

        private void Department_Combo_SelectedIndexChanged(object sender, EventArgs e)
        {
            this.get_notifications();
        }
    }
}
