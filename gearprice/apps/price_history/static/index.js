function populate_gear_list(brand_id)
{
	url_camera = "/api/v1/gear/?brand=" + brand_id + "&gear_type__name=camera&format=json";
	$("#camera-list").empty();
	$("#lens-list").empty();

	$("#gear-list").spin();

	$.getJSON(url_camera, function(data) {
		var items = [];
		var title = "";

		title = $("<h2>Camera List</h2>");

		if(data.objects.length == 0) return;

		$.each(data.objects, function(key, gear) {
			li = '<li><a href="#" onClick="load_gear_details(' + gear.id + ',\'' + gear.name + '\')">' + gear.name + "</a></li>";
			items.push(li);
		});

		var ul = $("<ul/>", { "class": "", html: items.join("")});

		$("#gear-list").spin(false);
		title.appendTo("#camera-list");
		ul.appendTo("#camera-list");
	});

	url_lens = "/api/v1/gear/?brand=" + brand_id + "&gear_type__name=lens&format=json";
	$.getJSON(url_lens, function(data) {
		var items = [];
		var title = "";

		title = $("<h2>Lens List</h2>");

		if(data.objects.length == 0) return;

		$.each(data.objects, function(key, gear) {
			li = '<li><a href="#" onClick="load_gear_details(' + gear.id + ',\'' + gear.name + '\')">' + gear.name + "</a></li>";
			items.push(li);
		});

		var ul = $("<ul/>", { "class": "", html: items.join("")});

		$("#gear-list").spin(false);
		title.appendTo("#lens-list");
		ul.appendTo("#lens-list");
	});
}


function load_gear_details(gear_id, gear_name)
{
	url = "/gear/" + gear_id + "/partial/";
	$("#gear-details").empty();
	$("#gear-details").spin();

	$("#gear-details").load(url, function() {
		$("#gear-details").spin(false);
		history.pushState('', gear_name, "/gear/"+gear_id+"/");

		document.title = gear_name;
		$(this).attr("title", gear_name);
	});
}


