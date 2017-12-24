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
    public partial class StudentMarksForm : Form
    {
        private List<server.Mark> Marks;

        public StudentMarksForm()
        {
            InitializeComponent();

            this.Marks = new List<server.Mark>();

            this.get_marks();
        }

        private void get_marks()
        {
            using (var DB = new LiteDatabase(@"StudyhoodData.db"))
            {
                var marks_col = DB.GetCollection<server.Mark>("marks");
                var marks_cont = marks_col.Find(x => x.Student_id == Student_Lab.Text);

                this.Marks.Clear();
                Marks_Table.Rows.Clear();

                foreach (server.Mark mark in marks_cont)
                {
                    this.Marks.Add(mark);
                }
                
                marks_col.EnsureIndex(x => x.Id);
            }

            this.update_content();
        }

        private void update_content()
        {
            Marks_Table.Rows.Clear();

            foreach (var mark in this.Marks)
            {
                if (mark.Discipline_id == Discipline_Combo.Text)
                {
                    var row = new string[] { mark.Date, mark.Work, mark.Name };
                    Marks_Table.Rows.Add(row);
                }   
            }
        }

        private void Discipline_Combo_SelectedIndexChanged(object sender, EventArgs e)
        {
            this.update_content();
        }
    }
}
