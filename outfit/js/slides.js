function themeSwitcher(themeName){
    alert("themeSwitcher ON");
    document.getElementById('theme').setAttribute('href','/PythonCourseNetIT-Slides/lib/reveal.js/css/theme/'+themeName+'.css');
}
function  PrettyPreCode(){
    var codeNodes = document.querySelectorAll('pre>code');

    for (var i = 0; i < codeNodes.length; i++)
    {
        var content = codeNodes[i].innerHTML;

        // get indent
        var indent =  content.match(/^\n*(\s*)/)[1];

        // remove indent from all lines
        var indentRE = new RegExp("^" + indent, "gm");
        content = content.replace(indentRE, "");

        // clean empty lines on start/end
        content = content.replace(/^\s*/,"");
        content = content.replace(/\s*$/, "");

        codeNodes[i].innerHTML = content;
        codeNodes[i].style.overflow="auto";
    }
}
function  PrettyPreCodeOld(){
    var codeNodes = document.querySelectorAll('pre>code');

    for (var i = 0; i < codeNodes.length; i++)
    {
        var content = codeNodes[i].innerHTML;
        // console.log("content:", content);

        var lines = content.split('\n');
        // console.log("lines:", lines);

        if ( !lines[1] ){
            continue;
        }
        var tab_index = lines[1].search(/\S/);
        // console.log("tab_index", tab_index);

        var contentNew = '';
        for ( var j=0; j<lines.length; j++ ){
            lines[j] = lines[j].substring(tab_index-1);
            contentNew += lines[j]+'\n';
        }

        codeNodes[i].innerHTML = contentNew;
        codeNodes[i].style.overflow="auto";
    }
}

function applyBackgrounds() {
    const bgPath = '../../../outfit/images/for_slides/'
    const mappings = {
        'presentation-title': bgPath+'presentation_title_slide_bg.png',
        'copyright': bgPath+'green_slide_bg.png',
        'main-section-title':bgPath+'blue_slide_bg.png',
        'sub-sections': bgPath+'normal_slide_bg.png',
        'end-slide':bgPath+'end_slide_bd.png'
    }

    for (const prop in mappings) {
        const nodes = document.querySelectorAll(`.${prop}`);
        for(const node of nodes){
            node.dataset.background = mappings[prop];
            node.dataset.backgroundTransition='slide'
        }

    }


}

PrettyPreCode();
applyBackgrounds()

