#!/usr/local/bin/python
# -*- coding: iso-8859-15 -*-
"""
BC (Border-Check) is a tool to retrieve info of traceroute tests over website navigation routes.
GPLv3 - 2013 by psy (epsylon@riseup.net)
"""
from xml.dom.minidom import parseString
# extract data from a xml file
file = open('data.xml','r')
data = file.read()
file.close()
dom = parseString(data)
xmlTag = dom.getElementsByTagName('travel')[0].toxml()
xmlData= xmlTag.replace('<travel>','').replace('</travel>','')
xmlHost = dom.getElementsByTagName('host')[0].toxml()
xmlIP = dom.getElementsByTagName('ip')[0].toxml()
xmlLongitude = dom.getElementsByTagName('longitude')[0].toxml()
xmlLatitude = dom.getElementsByTagName('latitude')[0].toxml()
xmlCity = dom.getElementsByTagName('city')[0].toxml()
xmlCountry = dom.getElementsByTagName('country')[0].toxml()
xmlServerName = dom.getElementsByTagName('server_name')[0].toxml()
xmlMeta = dom.getElementsByTagName('meta')[0].toxml()

output = """
<html>
<head>
  <title>Border Check - Web Visualizator</title>
   <link rel="stylesheet" href="js/leaflet/leaflet.css" />
   <link rel="stylesheet" href="style.css" />
    <script src="js/leaflet/leaflet.js"></script>
</head>
<body>
 <center>
  <table>
     <tr>
     <td><center><div id="map" style="width: 600px; height: 400px"></div></center></td>
	<script>
		var map = L.map('map').setView([23.505, -3.09], 18);
		L.tileLayer('Border Check', {
			maxZoom: 18,
			attribution: 'Map: <a href="http://openstreetmap.org">OpenStreetMap</a>'
		}).addTo(map);

		L.marker([51.5, -0.09]).addTo(map)
			.bindPopup("<b>"""+xmlMeta+"""</b><br />").openPopup();

		var popup = L.popup();
	</script>
    <br />
    </tr>
     <tr>
      <td>
       <center>
         <table border="1">
           <tr>
            <td><b>Host:</b></td>
            <td>"""+xmlHost+"""</td>
           </tr>
           <tr>
            <td><b>IP:</b></td>
            <td>"""+xmlIP+"""</td>
           </tr>
           <tr>
            <td><b>Coordinates:</b></td>
            <td>"""+xmlLongitude+""" : """+xmlLatitude+"""</td>
           </tr>
           <tr>
            <td><b>Server name:</b></td>
            <td>"""+xmlServerName+"""</td>
          </tr>
          <tr>
            <td><b>Country:</b></td>
            <td>"""+xmlCountry+"""</td>
          </tr>
          <tr>
            <td><b>City:</b></td>
            <td>"""+xmlCity+"""</td>
          </tr>
          <tr>
           <td><b>Metadata:</b></td>
         
         <td>"""+xmlMeta+"""</td>
         </tr>
     </table>
   </center>
   </td>
  </tr>
 </table>
</center>
</body>
</html>
"""
