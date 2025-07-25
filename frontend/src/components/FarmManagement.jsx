import { useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Label } from '@/components/ui/label.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { 
  MapPin, 
  Plus, 
  Ruler, 
  Droplets,
  Thermometer,
  Calendar,
  Tractor,
  Home,
  BarChart3,
  Map,
  Leaf,
  Award
} from 'lucide-react'

export function FarmManagement() {
  const [activeTab, setActiveTab] = useState('overview')
  
  const farmData = {
    name: 'Okafor Family Farm',
    location: 'Igbo-Ukwu, Anambra State',
    totalArea: '5.2 hectares',
    ownership: 'Family Land (Customary)',
    established: '1987',
    plots: 8,
    activeSeasons: 2
  }

  const plots = [
    {
      id: 1,
      name: 'Ubi Plot (Yam Field)',
      area: '1.2 hectares',
      soilType: 'Sandy Loam',
      currentCrop: 'White Yam',
      status: 'Growing',
      plantingDate: '2024-04-15',
      expectedHarvest: '2024-12-15'
    },
    {
      id: 2,
      name: 'Akpu Plot (Cassava Field)',
      area: '0.8 hectares',
      soilType: 'Clay Loam',
      currentCrop: 'Cassava',
      status: 'Mature',
      plantingDate: '2023-06-10',
      expectedHarvest: '2024-08-10'
    },
    {
      id: 3,
      name: 'Ugwu Plot (Vegetable Garden)',
      area: '0.3 hectares',
      soilType: 'Rich Loam',
      currentCrop: 'Fluted Pumpkin',
      status: 'Harvesting',
      plantingDate: '2024-05-01',
      expectedHarvest: '2024-07-30'
    }
  ]

  const livestock = [
    {
      id: 1,
      type: 'Goats',
      breed: 'West African Dwarf',
      count: 12,
      status: 'Healthy',
      lastCheckup: '2024-07-15'
    },
    {
      id: 2,
      type: 'Chickens',
      breed: 'Local Breed',
      count: 25,
      status: 'Healthy',
      lastCheckup: '2024-07-20'
    }
  ]

  const equipment = [
    {
      id: 1,
      name: 'Cutlass (Traditional)',
      type: 'Hand Tool',
      condition: 'Good',
      lastMaintenance: '2024-06-01'
    },
    {
      id: 2,
      name: 'Hoe (Traditional)',
      type: 'Hand Tool',
      condition: 'Excellent',
      lastMaintenance: '2024-05-15'
    },
    {
      id: 3,
      name: 'Water Pump',
      type: 'Irrigation',
      condition: 'Fair',
      lastMaintenance: '2024-03-20'
    }
  ]

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white">Farm Management</h2>
          <p className="text-gray-600 dark:text-gray-400">
            Traditional land management with modern geospatial mapping
          </p>
        </div>
        <Button className="bg-green-600 hover:bg-green-700">
          <Plus className="h-4 w-4 mr-2" />
          Add Plot
        </Button>
      </div>

      {/* Farm Overview Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center space-x-2">
              <Ruler className="h-5 w-5 text-green-600" />
              <div>
                <p className="text-sm text-gray-600 dark:text-gray-400">Total Area</p>
                <p className="text-lg font-bold">{farmData.totalArea}</p>
              </div>
            </div>
          </CardContent>
        </Card>
        
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center space-x-2">
              <Map className="h-5 w-5 text-blue-600" />
              <div>
                <p className="text-sm text-gray-600 dark:text-gray-400">Active Plots</p>
                <p className="text-lg font-bold">{farmData.plots}</p>
              </div>
            </div>
          </CardContent>
        </Card>
        
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center space-x-2">
              <Calendar className="h-5 w-5 text-orange-600" />
              <div>
                <p className="text-sm text-gray-600 dark:text-gray-400">Active Seasons</p>
                <p className="text-lg font-bold">{farmData.activeSeasons}</p>
              </div>
            </div>
          </CardContent>
        </Card>
        
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center space-x-2">
              <Home className="h-5 w-5 text-purple-600" />
              <div>
                <p className="text-sm text-gray-600 dark:text-gray-400">Established</p>
                <p className="text-lg font-bold">{farmData.established}</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
        <TabsList className="grid w-full grid-cols-6">
          <TabsTrigger value="overview">Overview</TabsTrigger>
          <TabsTrigger value="plots">Plots</TabsTrigger>
          <TabsTrigger value="livestock">Livestock</TabsTrigger>
          <TabsTrigger value="equipment">Equipment</TabsTrigger>
          <TabsTrigger value="mapping">Mapping</TabsTrigger>
          <TabsTrigger value="analytics">Analytics</TabsTrigger>
        </TabsList>

        {/* Overview Tab */}
        <TabsContent value="overview" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>Farm Information</CardTitle>
              <CardDescription>Basic farm details and ownership information</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label htmlFor="farmName">Farm Name</Label>
                  <Input id="farmName" value={farmData.name} />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="location">Location</Label>
                  <div className="flex items-center space-x-2">
                    <MapPin className="h-4 w-4 text-gray-500" />
                    <Input id="location" value={farmData.location} />
                  </div>
                </div>
                <div className="space-y-2">
                  <Label htmlFor="ownership">Land Ownership Type</Label>
                  <select className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm">
                    <option value="family">Family Land (Customary)</option>
                    <option value="communal">Communal Land</option>
                    <option value="leased">Leased Land</option>
                    <option value="purchased">Purchased Land</option>
                  </select>
                </div>
                <div className="space-y-2">
                  <Label htmlFor="totalArea">Total Area</Label>
                  <Input id="totalArea" value={farmData.totalArea} />
                </div>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Plots Tab */}
        <TabsContent value="plots" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center space-x-2">
                <Map className="h-5 w-5" />
                <span>Plot Management</span>
              </CardTitle>
              <CardDescription>
                Manage individual plots with traditional boundaries and modern mapping
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {plots.map((plot) => (
                  <Card key={plot.id} className="border-2">
                    <CardHeader className="pb-3">
                      <div className="flex items-center justify-between">
                        <CardTitle className="text-lg">{plot.name}</CardTitle>
                        <Badge variant={
                          plot.status === 'Growing' ? 'default' :
                          plot.status === 'Mature' ? 'secondary' :
                          'destructive'
                        }>
                          {plot.status}
                        </Badge>
                      </div>
                    </CardHeader>
                    <CardContent className="space-y-3">
                      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                        <div>
                          <span className="text-gray-600">Area:</span>
                          <p className="font-medium">{plot.area}</p>
                        </div>
                        <div>
                          <span className="text-gray-600">Soil Type:</span>
                          <p className="font-medium">{plot.soilType}</p>
                        </div>
                        <div>
                          <span className="text-gray-600">Current Crop:</span>
                          <p className="font-medium">{plot.currentCrop}</p>
                        </div>
                        <div>
                          <span className="text-gray-600">Expected Harvest:</span>
                          <p className="font-medium">{plot.expectedHarvest}</p>
                        </div>
                      </div>
                      <div className="flex justify-end space-x-2">
                        <Button size="sm" variant="outline">
                          <Map className="h-4 w-4 mr-1" />
                          View Map
                        </Button>
                        <Button size="sm" variant="outline">
                          Edit Plot
                        </Button>
                      </div>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Livestock Tab */}
        <TabsContent value="livestock" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>Livestock Management</CardTitle>
              <CardDescription>
                Track indigenous breeds with traditional management practices
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {livestock.map((animal) => (
                  <Card key={animal.id} className="border-2">
                    <CardHeader className="pb-3">
                      <div className="flex items-center justify-between">
                        <CardTitle className="text-lg">{animal.type}</CardTitle>
                        <Badge variant="default">{animal.status}</Badge>
                      </div>
                    </CardHeader>
                    <CardContent className="space-y-2">
                      <div className="flex justify-between text-sm">
                        <span className="text-gray-600">Breed:</span>
                        <span className="font-medium">{animal.breed}</span>
                      </div>
                      <div className="flex justify-between text-sm">
                        <span className="text-gray-600">Count:</span>
                        <span className="font-medium">{animal.count}</span>
                      </div>
                      <div className="flex justify-between text-sm">
                        <span className="text-gray-600">Last Checkup:</span>
                        <span className="font-medium">{animal.lastCheckup}</span>
                      </div>
                      <Button className="w-full mt-4" size="sm">
                        View Details
                      </Button>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Equipment Tab */}
        <TabsContent value="equipment" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center space-x-2">
                <Tractor className="h-5 w-5" />
                <span>Equipment & Tools</span>
              </CardTitle>
              <CardDescription>
                Traditional tools and modern equipment tracking
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {equipment.map((item) => (
                  <div key={item.id} className="flex items-center justify-between p-4 border rounded-lg">
                    <div className="flex items-center space-x-3">
                      <Tractor className="h-8 w-8 text-gray-600" />
                      <div>
                        <h4 className="font-medium">{item.name}</h4>
                        <p className="text-sm text-gray-600">{item.type}</p>
                      </div>
                    </div>
                    <div className="text-right">
                      <Badge variant={
                        item.condition === 'Excellent' ? 'default' :
                        item.condition === 'Good' ? 'secondary' :
                        'destructive'
                      }>
                        {item.condition}
                      </Badge>
                      <p className="text-xs text-gray-500 mt-1">
                        Last maintained: {item.lastMaintenance}
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Mapping Tab */}
        <TabsContent value="mapping" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>Geospatial Mapping</CardTitle>
              <CardDescription>
                Traditional boundaries with GPS precision mapping
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="bg-gray-100 dark:bg-gray-800 rounded-lg p-8 text-center">
                <Map className="h-16 w-16 mx-auto text-gray-400 mb-4" />
                <h3 className="text-lg font-medium mb-2">Interactive Farm Map</h3>
                <p className="text-gray-600 dark:text-gray-400 mb-4">
                  View your farm plots with satellite imagery and traditional boundary markers
                </p>
                <Button className="bg-green-600 hover:bg-green-700">
                  Launch Map View
                </Button>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Analytics Tab */}
        <TabsContent value="analytics" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center space-x-2">
                <BarChart3 className="h-5 w-5" />
                <span>Farm Analytics</span>
              </CardTitle>
              <CardDescription>
                Sustainability metrics with cultural indicators
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <Card className="bg-green-50 dark:bg-green-900/20">
                  <CardContent className="p-4 text-center">
                    <Leaf className="h-8 w-8 mx-auto text-green-600 mb-2" />
                    <h4 className="font-medium text-green-800 dark:text-green-200">
                      Soil Health Score
                    </h4>
                    <p className="text-2xl font-bold text-green-600">85%</p>
                    <p className="text-xs text-green-700 dark:text-green-300">
                      Excellent traditional practices
                    </p>
                  </CardContent>
                </Card>
                
                <Card className="bg-blue-50 dark:bg-blue-900/20">
                  <CardContent className="p-4 text-center">
                    <Droplets className="h-8 w-8 mx-auto text-blue-600 mb-2" />
                    <h4 className="font-medium text-blue-800 dark:text-blue-200">
                      Water Efficiency
                    </h4>
                    <p className="text-2xl font-bold text-blue-600">92%</p>
                    <p className="text-xs text-blue-700 dark:text-blue-300">
                      Traditional conservation methods
                    </p>
                  </CardContent>
                </Card>
                
                <Card className="bg-orange-50 dark:bg-orange-900/20">
                  <CardContent className="p-4 text-center">
                    <Award className="h-8 w-8 mx-auto text-orange-600 mb-2" />
                    <h4 className="font-medium text-orange-800 dark:text-orange-200">
                      Productivity Index
                    </h4>
                    <p className="text-2xl font-bold text-orange-600">78%</p>
                    <p className="text-xs text-orange-700 dark:text-orange-300">
                      Above regional average
                    </p>
                  </CardContent>
                </Card>
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  )
}

