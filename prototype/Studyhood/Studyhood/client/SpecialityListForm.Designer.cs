namespace Studyhood.client
{
    partial class SpecialityListForm
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
            this.Speciality_Combo = new System.Windows.Forms.ComboBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(183, 13);
            this.label1.TabIndex = 3;
            this.label1.Text = "Специальность и форма обучения:";
            // 
            // Speciality_Combo
            // 
            this.Speciality_Combo.FormattingEnabled = true;
            this.Speciality_Combo.Items.AddRange(new object[] {
            "Информатика и вычислительная техника (09.03.01 – очная, бакалавриат, аккредитован" +
                "о)",
            "Информационные системы и технологии (09.03.02 – очная, бакалавриат, аккредитовано" +
                ")",
            "Программная инженерия (09.03.04 – очная, бакалавриат, аккредитовано)",
            "Информационная безопасность (10.03.01 – очная, бакалавриат, аккредитовано)"});
            this.Speciality_Combo.Location = new System.Drawing.Point(12, 25);
            this.Speciality_Combo.Name = "Speciality_Combo";
            this.Speciality_Combo.Size = new System.Drawing.Size(618, 21);
            this.Speciality_Combo.TabIndex = 2;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 52);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.ReadOnly = true;
            this.richTextBox1.Size = new System.Drawing.Size(618, 248);
            this.richTextBox1.TabIndex = 4;
            this.richTextBox1.Text = "<Описание направления и т.п.>";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(555, 306);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 5;
            this.button1.Text = "Записаться";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.open_enrollee_sign_in_form);
            // 
            // SpecialityListForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(642, 341);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.Speciality_Combo);
            this.Name = "SpecialityListForm";
            this.Text = "SpecialityListForm";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox Speciality_Combo;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
    }
}