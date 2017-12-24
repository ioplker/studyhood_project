using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Studyhood.server
{
    class Plan
    {
        public Guid Id { get; set; }
        public String Semester { get; set; }
        public String Discipline_id { get; set; }
        public String Speciality_id { get; set; }
    }
}
