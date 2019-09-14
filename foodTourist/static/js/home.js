$(document).ready(function () {
    console.log("ready!")

    $(function(){
        $('.stop-field-new').on('input', function() {
            let $this = $(this)
            let $clone = $this.clone()
            let name = $clone.find("input").attr('name')
            let n = parseInt(name.split('_')[1]) + 1
            name = 'stop_' + n
            $clone.find("input").val('')
            $clone.find("input").attr('name', name)
            $clone.find("input").attr('id', 'id_' + name)
            $clone.find("label").attr('id', 'id_' + name)
            $clone.find("label").attr('for', 'id_' + name)
            $clone.find("label").text("Stop " + n + ": ")
            console.log($this.parent().html())
            $this.removeClass('stop-field-new')
            console.log($this.parent().html())
            $clone.appendTo($this.parent())
            console.log($this.parent().html())
            $this.off('input', arguments.callee)
            $clone.on('input', arguments.callee)
        });
    });

    
});





// $("#add-another-stop").click(function() {
//     //form_count ++;

//     element = $('<input type="text"/>');
//     element.attr('name', 'extra_field_' + form_count);
//     $("#forms").append(element);
//     // build element and append it to our forms container

//     $("[name=extra_field_count]").val(form_count);
//     // increment form count so our view knows to populate 
//     // that many fields for validation
// })
