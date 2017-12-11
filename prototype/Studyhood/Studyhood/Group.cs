using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Studyhood
{
    class Group
    {
        public Guid Id { get; set; }
        public Guid Speciality_id { get; set; }
        public String Code { get; set; }
        public String Course { get; set; }
    }
}
