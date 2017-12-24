using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Studyhood.server
{
    class Mark
    {
        public Guid Id { get; set; }
        public String Student_id { get; set; }
        public String Teacher_id { get; set; }
        public String Discipline_id { get; set; }
        public String Date { get; set; }
        public String Rating_type_id { get; set; }        
        public String Work { get; set; }
        public String Name { get; set; }
    }
}
