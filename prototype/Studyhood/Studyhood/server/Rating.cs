using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Studyhood
{
    class Rating
    {
        public Guid Discipline_id { get; set; }
        public Guid Student_id { get; set; }
        public Guid Rating_type_id { get; set; }
        public Guid Mark_id { get; set; }
        public Guid Professor_id { get; set; }
        public DateTime Date { get; set; }
    }
}
