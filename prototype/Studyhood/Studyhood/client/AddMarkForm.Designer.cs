namespace Studyhood.client
{
    partial class AddMarkForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Teacher_Lab = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.Discipline_Combo = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.Mark_Combo = new System.Windows.Forms.ComboBox();
            this.label3 = new System.Windows.Forms.Label();
            this.Work_Edit = new System.Windows.Forms.TextBox();
            this.Date_Picker = new System.Windows.Forms.DateTimePicker();
            this.label1 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.Student_Combo = new System.Windows.Forms.ComboBox();
            this.label7 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.RatingType_Combo = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
            // 
            // Teacher_Lab
            // 
            this.Teacher_Lab.AutoSize = true;
            this.Teacher_Lab.Location = new System.Drawing.Point(12, 28);
            this.Teacher_Lab.Name = "Teacher_Lab";
            this.Teacher_Lab.Size = new System.Drawing.Size(162, 13);
            this.Teacher_Lab.TabIndex = 21;
            this.Teacher_Lab.Text = "Тараканов Семён Николаевич";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 9);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(89, 13);
            this.label4.TabIndex = 20;
            this.label4.Text = "Преподаватель:";
            // 
            // Discipline_Combo
            // 
            this.Discipline_Combo.FormattingEnabled = true;
            this.Discipline_Combo.Items.AddRange(new object[] {
            "Русский язык",
            "Вычислительная математика",
            "Сети и телекоммуникации",
            "Экономика",
            "Философия"});
            this.Discipline_Combo.Location = new System.Drawing.Point(91, 84);
            this.Discipline_Combo.Name = "Discipline_Combo";
            this.Discipline_Combo.Size = new System.Drawing.Size(341, 21);
            this.Discipline_Combo.TabIndex = 19;
            this.Discipline_Combo.Text = "Философия";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 87);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(73, 13);
            this.label2.TabIndex = 16;
            this.label2.Text = "Дисциплина:";
            // 
            // Mark_Combo
            // 
            this.Mark_Combo.FormattingEnabled = true;
            this.Mark_Combo.Items.AddRange(new object[] {
            "неуд.",
            "уд.",
            "хорошо",
            "отлично"});
            this.Mark_Combo.Location = new System.Drawing.Point(91, 163);
            this.Mark_Combo.Name = "Mark_Combo";
            this.Mark_Combo.Size = new System.Drawing.Size(128, 21);
            this.Mark_Combo.TabIndex = 23;
            this.Mark_Combo.Text = "хорошо";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 114);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(46, 13);
            this.label3.TabIndex = 22;
            this.label3.Text = "Работа:";
            // 
            // Work_Edit
            // 
            this.Work_Edit.Location = new System.Drawing.Point(91, 111);
            this.Work_Edit.Name = "Work_Edit";
            this.Work_Edit.Size = new System.Drawing.Size(341, 20);
            this.Work_Edit.TabIndex = 24;
            this.Work_Edit.Text = "Конфликт и его решения";
            // 
            // Date_Picker
            // 
            this.Date_Picker.Format = System.Windows.Forms.DateTimePickerFormat.Short;
            this.Date_Picker.Location = new System.Drawing.Point(304, 137);
            this.Date_Picker.Name = "Date_Picker";
            this.Date_Picker.Size = new System.Drawing.Size(128, 20);
            this.Date_Picker.TabIndex = 25;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(262, 143);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(36, 13);
            this.label1.TabIndex = 26;
            this.label1.Text = "Дата:";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(12, 166);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(48, 13);
            this.label6.TabIndex = 27;
            this.label6.Text = "Оценка:";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(15, 190);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 28;
            this.button1.Text = "Поставить";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.add_mark);
            // 
            // Student_Combo
            // 
            this.Student_Combo.FormattingEnabled = true;
            this.Student_Combo.Location = new System.Drawing.Point(91, 57);
            this.Student_Combo.Name = "Student_Combo";
            this.Student_Combo.Size = new System.Drawing.Size(341, 21);
            this.Student_Combo.TabIndex = 30;
            this.Student_Combo.Text = "Иванова Иоанна Ивановна";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(12, 60);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(50, 13);
            this.label7.TabIndex = 29;
            this.label7.Text = "Студент:";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(12, 140);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(62, 13);
            this.label8.TabIndex = 32;
            this.label8.Text = "Вид оцеки:";
            // 
            // RatingType_Combo
            // 
            this.RatingType_Combo.FormattingEnabled = true;
            this.RatingType_Combo.Items.AddRange(new object[] {
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8"});
            this.RatingType_Combo.Location = new System.Drawing.Point(91, 137);
            this.RatingType_Combo.Name = "RatingType_Combo";
            this.RatingType_Combo.Size = new System.Drawing.Size(128, 21);
            this.RatingType_Combo.TabIndex = 31;
            this.RatingType_Combo.Text = "5-балльная";
            // 
            // AddMarkForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(444, 225);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.RatingType_Combo);
            this.Controls.Add(this.Student_Combo);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.Date_Picker);
            this.Controls.Add(this.Work_Edit);
            this.Controls.Add(this.Mark_Combo);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.Teacher_Lab);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.Discipline_Combo);
            this.Controls.Add(this.label2);
            this.Name = "AddMarkForm";
            this.Text = "AddMarkForm";
            this.Load += new System.EventHandler(this.AddMarkForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label Teacher_Lab;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.ComboBox Discipline_Combo;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ComboBox Mark_Combo;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox Work_Edit;
        private System.Windows.Forms.DateTimePicker Date_Picker;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.ComboBox Student_Combo;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.ComboBox RatingType_Combo;
    }
}