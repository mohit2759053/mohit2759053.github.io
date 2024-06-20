
    $(document).ready(function(){

        $(".triggersearch").click(function(){
            $(".searchbox").toggle();
            $("input[type='text']").focus();
        })


        $(".uppertrigger").click(function(){
            $(".upsearchbox").toggle();
            $("input[type='text']").focus();
        })


        // $( ".triggersearch" ).click(function() {
        //     $( ".navbar" ).css( "background","#45474b" );
        //     $(".navbar").focus();

        // })
    })
