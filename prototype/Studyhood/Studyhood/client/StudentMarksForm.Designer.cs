namespace Studyhood.client
{
    partial class StudentMarksForm
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
            this.label1 = new System.Windows.Forms.Label();
            this.Marks_Table = new System.Windows.Forms.DataGridView();
            this.Column1 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Column2 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Column3 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Discipline_Combo = new System.Windows.Forms.ComboBox();
            this.Semester_Combo = new System.Windows.Forms.ComboBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.Teacher_Lab = new System.Windows.Forms.Label();
            this.Student_Lab = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.Marks_Table)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(9, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(50, 13);
            this.label1.TabIndex = 3;
            this.label1.Text = "Студент:";
            // 
            // Marks_Table
            // 
            this.Marks_Table.AllowUserToAddRows = false;
            this.Marks_Table.AllowUserToDeleteRows = false;
            this.Marks_Table.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.Marks_Table.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.Column1,
            this.Column2,
            this.Column3});
            this.Marks_Table.Location = new System.Drawing.Point(12, 79);
            this.Marks_Table.Name = "Marks_Table";
            this.Marks_Table.ReadOnly = true;
            this.Marks_Table.Size = new System.Drawing.Size(565, 186);
            this.Marks_Table.TabIndex = 13;
            // 
            // Column1
            // 
            this.Column1.HeaderText = "Дата";
            this.Column1.Name = "Column1";
            this.Column1.ReadOnly = true;
            // 
            // Column2
            // 
            this.Column2.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.Fill;
            this.Column2.HeaderText = "Работа";
            this.Column2.Name = "Column2";
            this.Column2.ReadOnly = true;
            // 
            // Column3
            // 
            this.Column3.HeaderText = "Оценка";
            this.Column3.Name = "Column3";
            this.Column3.ReadOnly = true;
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
            this.Discipline_Combo.Location = new System.Drawing.Point(234, 52);
            this.Discipline_Combo.Name = "Discipline_Combo";
            this.Discipline_Combo.Size = new System.Drawing.Size(343, 21);
            this.Discipline_Combo.TabIndex = 12;
            this.Discipline_Combo.Text = "Философия";
            this.Discipline_Combo.SelectedIndexChanged += new System.EventHandler(this.Discipline_Combo_SelectedIndexChanged);
            // 
            // Semester_Combo
            // 
            this.Semester_Combo.FormattingEnabled = true;
            this.Semester_Combo.Items.AddRange(new object[] {
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8"});
            this.Semester_Combo.Location = new System.Drawing.Point(72, 52);
            this.Semester_Combo.Name = "Semester_Combo";
            this.Semester_Combo.Size = new System.Drawing.Size(58, 21);
            this.Semester_Combo.TabIndex = 11;
            this.Semester_Combo.Text = "5";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(9, 55);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(54, 13);
            this.label3.TabIndex = 10;
            this.label3.Text = "Семестр:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(155, 55);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(73, 13);
            this.label2.TabIndex = 9;
            this.label2.Text = "Дисциплина:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(368, 9);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(89, 13);
            this.label4.TabIndex = 14;
            this.label4.Text = "Преподаватель:";
            // 
            // Teacher_Lab
            // 
            this.Teacher_Lab.AutoSize = true;
            this.Teacher_Lab.Location = new System.Drawing.Point(368, 28);
            this.Teacher_Lab.Name = "Teacher_Lab";
            this.Teacher_Lab.Size = new System.Drawing.Size(162, 13);
            this.Teacher_Lab.TabIndex = 15;
            this.Teacher_Lab.Text = "Тараканов Семён Николаевич";
            // 
            // Student_Lab
            // 
            this.Student_Lab.AutoSize = true;
            this.Student_Lab.Location = new System.Drawing.Point(9, 28);
            this.Student_Lab.Name = "Student_Lab";
            this.Student_Lab.Size = new System.Drawing.Size(145, 13);
            this.Student_Lab.TabIndex = 16;
            this.Student_Lab.Text = "Иванова Иоанна Ивановна";
            // 
            // StudentMarksForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(589, 277);
            this.Controls.Add(this.Student_Lab);
            this.Controls.Add(this.Teacher_Lab);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.Marks_Table);
            this.Controls.Add(this.Discipline_Combo);
            this.Controls.Add(this.Semester_Combo);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "StudentMarksForm";
            this.Text = "StudentMarksForm";
            ((System.ComponentModel.ISupportInitialize)(this.Marks_Table)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.DataGridView Marks_Table;
        private System.Windows.Forms.ComboBox Discipline_Combo;
        private System.Windows.Forms.ComboBox Semester_Combo;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label Teacher_Lab;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column1;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column2;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column3;
        private System.Windows.Forms.Label Student_Lab;
    }
}