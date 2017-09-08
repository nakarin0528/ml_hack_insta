var pictureCount = 100
var intervalID = window.setInterval(function() {

    if(document.getElementsByClassName("_mck9w _gvoze _f2mse").length < pictureCount){
        console.log("scrolled bottom")
        window.scrollTo(0,document.body.scrollHeight);

        setTimeout(function(){
                        console.log("scrolled top");
                        window.scrollTo(0,0);
                    },250);
    } else {
        clearInterval(intervalID);
        alert("Finished!")
        var links = []
        if (confirm("Export data")){
            var imgs = document.getElementsByClassName("_mck9w _gvoze _f2mse")
            for (var i=0; i < imgs.length; i+=1){
            // for ( img in imgs){
                links.push(imgs[i].children[0].href);
            }
            console.log(links)
        }
    }

}, 500);
