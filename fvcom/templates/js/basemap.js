        var map, layer;
            function init(){

                //map = new OpenLayers.Map('map');
                map = new OpenLayers.Map('map',{
                                                layers: [
                                                         new OpenLayers.Layer.XYZ(
                                                        'ESRI Ocean'
                                                        ,'http://services.arcgisonline.com/ArcGIS/rest/services/Ocean_Basemap/MapServer/tile/${z}/${y}/${x}.jpg'
                                                        ,{
                                                          sphericalMercator : true
                                                          ,visibility        : 1
                                                          ,isBaseLayer       : true
                                                          ,opacity           : 1
                                                          ,wrapDateLine      : true
                                                          ,attribution       : "GEBCO, NOAA, National Geographic, AND data by <a href='http://www.arcgis.com/home/item.html?id=6348e67824504fc9a62976434bf0d8d5'>ESRI</a>"
                                                          }
                                                                                   ),
                                                         new OpenLayers.Layer.OSM(),

                                                        ]
                                            ,projection        : "EPSG:3857"
                                            ,displayProjection : "EPSG:4326"
                                            ,units             : "m"
                                            ,maxExtent         : new OpenLayers.Bounds(-20037508,-20037508,20037508,20037508.34)
                                       });

                

                CGridTest = new OpenLayers.Layer.WMS("CGridTest",
                                                "/wms/datasets/CGridTest/",
                                                {
                                                    layers:"u,v",
                                                    transparent: true,
                                                    styles: 'vectors_average_jet_None_None_cell_False',
                                                    time: "",
                                                    elevation: "0"
                                                },

                                                {
                                                    singleTile: true
                                                    ,
                                                    ratio: 1,
                                                    isBaseLayer: false,
                                                    visibility: false

                                                }
                                                );
                map.addLayer(CGridTest);
                

                UGridTest = new OpenLayers.Layer.WMS("UGridTest",
                                                "/wms/datasets/UGridTest/",
                                                {
                                                    layers:"u,v",
                                                    transparent: true,
                                                    styles: 'vectors_average_jet_None_None_cell_False',
                                                    time: "",
                                                    elevation: "0"
                                                },

                                                {
                                                    singleTile: true
                                                    ,
                                                    ratio: 1,
                                                    isBaseLayer: false,
                                                    visibility: false

                                                }
                                                );
                map.addLayer(UGridTest);
                

                GOM3 = new OpenLayers.Layer.WMS("GOM3",
                                                "/wms/datasets/GOM3/",
                                                {
                                                    layers:"salinity",
                                                    transparent: true,
                                                    styles: 'facets_average_jet_0_32_node_False',
                                                    time: "",
                                                    elevation: "0"
                                                },

                                                {
                                                    singleTile: true
                                                    ,
                                                    ratio: 1,
                                                    isBaseLayer: false,
                                                    visibility: false

                                                }
                                                );
                map.addLayer(GOM3);
                

                map.setCenter(
                    new OpenLayers.LonLat(-67, 42).transform(
                        new OpenLayers.Projection("EPSG:4326"),
                        map.getProjectionObject()
                    ), 7
                );

                map.addControl(new OpenLayers.Control.LayerSwitcher());
            }
