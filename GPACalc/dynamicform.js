function dynamicdropdown(listindex)
{
    document.getElementById("subcategory").length = 0;
    switch (listindex)
    {
        case "2.5" :
            document.getElementById("subcategory").options[0]=new Option("Select","");
            document.getElementById("subcategory").options[1]=new Option("AP/Honors","AP/Honors");
            document.getElementById("subcategory").options[2]=new Option("College Prep (Regular)","College Prep (Regular)");
            break;

        case "5" :
        document.getElementById("subcategory").options[0]=new Option("Select","");
        document.getElementById("subcategory").options[1]=new Option("AP/Honors","AP/Honors");
        document.getElementById("subcategory").options[2]=new Option("College Prep (Regular)","College Prep (Regular)");
            break;
        case "6" :
            document.getElementById("subcategory").options[0]=new Option("AP/Honors","AP/Honors");
    }
    return true;
}
