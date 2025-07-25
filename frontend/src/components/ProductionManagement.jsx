import { useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Label } from '@/components/ui/label.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { Progress } from '@/components/ui/progress.jsx'
import { 
  Sprout, 
  Calendar, 
  Droplets,
  Bug,
  Scissors,
  Package,
  Heart,
  Milk,
  Egg,
  Beef,
  BarChart3,
  CheckCircle,
  AlertTriangle,
  Moon,
  Sun,
  Thermometer
} from 'lucide-react'

export function ProductionManagement() {
  const [activeTab, setActiveTab] = useState('planting')
  
  const plantingActivities = [
    {
      id: 1,
      crop: 'White Yam (Ubi Ọcha)',
      plot: 'Ubi Plot',
      plantingDate: '2024-04-15',
      method: 'Traditional Mounding',
      moonPhase: 'Waxing Moon',
      seedSource: 'Local Variety - Saved Seeds',
      status: 'Growing',
      progress: 65
    },
    {
      id: 2,
      crop: 'Cassava (Akpu)',
      plot: 'Akpu Plot',
      plantingDate: '2023-06-10',
      method: 'Ridge Planting',
      moonPhase: 'New Moon',
      seedSource: 'Improved Variety - TMS 30572',
      status: 'Mature',
      progress: 95
    }
  ]

  const cropMonitoring = [
    {
      id: 1,
      crop: 'White Yam',
      stage: 'Tuber Formation',
      health: 'Excellent',
      vigor: 85,
      lastInspection: '2024-07-20',
      traditionalIndicators: 'Leaves turning yellow (good sign)',
      weatherConditions: 'Adequate rainfall'
    },
    {
      id: 2,
      crop: 'Fluted Pumpkin',
      stage: 'Flowering',
      health: 'Good',
      vigor: 78,
      lastInspection: '2024-07-22',
      traditionalIndicators: 'Strong vine growth',
      weatherConditions: 'Hot and humid'
    }
  ]

  const pestManagement = [
    {
      id: 1,
      crop: 'Cassava',
      pest: 'Cassava Mosaic Disease',
      severity: 'Low',
      treatment: 'Neem Oil + Traditional Herbs',
      applicationDate: '2024-07-15',
      effectiveness: 'Good',
      cost: '₦2,500'
    },
    {
      id: 2,
      crop: 'Yam',
      pest: 'Yam Beetle',
      severity: 'Medium',
      treatment: 'Wood Ash + Pepper Solution',
      applicationDate: '2024-07-18',
      effectiveness: 'Excellent',
      cost: '₦1,200'
    }
  ]

  const livestockProduction = [
    {
      id: 1,
      type: 'Goats',
      breed: 'West African Dwarf',
      count: 12,
      milkProduction: '2.5L/day',
      lastBreeding: '2024-05-15',
      expectedKidding: '2024-10-15',
      healthStatus: 'Excellent'
    },
    {
      id: 2,
      type: 'Chickens',
      breed: 'Local Breed',
      count: 25,
      eggProduction: '18 eggs/day',
      lastVaccination: '2024-06-01',
      mortalityRate: '4%',
      healthStatus: 'Good'
    }
  ]

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white">Production Management</h2>
          <p className="text-gray-600 dark:text-gray-400">
            Complete crop and livestock production lifecycle tracking
          </p>
        </div>
        <Button className="bg-orange-600 hover:bg-orange-700">
          <Sprout className="h-4 w-4 mr-2" />
          New Activity
        </Button>
      </div>

      {/* Production Overview Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center space-x-2">
              <Sprout className="h-5 w-5 text-green-600" />
              <div>
                <p className="text-sm text-gray-600 dark:text-gray-400">Active Crops</p>
                <p className="text-lg font-bold">6</p>
              </div>
            </div>
          </CardContent>
        </Card>
        
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center space-x-2">
              <Heart className="h-5 w-5 text-red-600" />
              <div>
                <p className="text-sm text-gray-600 dark:text-gray-400">Livestock</p>
                <p className="text-lg font-bold">37</p>
              </div>
            </div>
          </CardContent>
        </Card>
        
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center space-x-2">
              <Calendar className="h-5 w-5 text-blue-600" />
              <div>
                <p className="text-sm text-gray-600 dark:text-gray-400">This Season</p>
                <p className="text-lg font-bold">2024 Rainy</p>
              </div>
            </div>
          </CardContent>
        </Card>
        
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center space-x-2">
              <Package className="h-5 w-5 text-purple-600" />
              <div>
                <p className="text-sm text-gray-600 dark:text-gray-400">Expected Harvest</p>
                <p className="text-lg font-bold">3.2 tons</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
        <TabsList className="grid w-full grid-cols-6">
          <TabsTrigger value="planting">Planting</TabsTrigger>
          <TabsTrigger value="monitoring">Monitoring</TabsTrigger>
          <TabsTrigger value="pest">Pest Control</TabsTrigger>
          <TabsTrigger value="harvest">Harvest</TabsTrigger>
          <TabsTrigger value="livestock">Livestock</TabsTrigger>
          <TabsTrigger value="records">Records</TabsTrigger>
        </TabsList>

        {/* Planting Activities Tab */}
        <TabsContent value="planting" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center space-x-2">
                <Sprout className="h-5 w-5" />
                <span>Planting Activities</span>
              </CardTitle>
              <CardDescription>
                Track planting with traditional methods and moon phase timing
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {plantingActivities.map((activity) => (
                  <Card key={activity.id} className="border-2">
                    <CardHeader className="pb-3">
                      <div className="flex items-center justify-between">
                        <CardTitle className="text-lg">{activity.crop}</CardTitle>
                        <Badge variant={
                          activity.status === 'Growing' ? 'default' :
                          activity.status === 'Mature' ? 'secondary' :
                          'destructive'
                        }>
                          {activity.status}
                        </Badge>
                      </div>
                    </CardHeader>
                    <CardContent className="space-y-4">
                      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                        <div>
                          <span className="text-gray-600">Plot:</span>
                          <p className="font-medium">{activity.plot}</p>
                        </div>
                        <div>
                          <span className="text-gray-600">Planting Date:</span>
                          <p className="font-medium">{activity.plantingDate}</p>
                        </div>
                        <div className="flex items-center space-x-1">
                          <Moon className="h-4 w-4 text-gray-600" />
                          <div>
                            <span className="text-gray-600">Moon Phase:</span>
                            <p className="font-medium">{activity.moonPhase}</p>
                          </div>
                        </div>
                        <div>
                          <span className="text-gray-600">Method:</span>
                          <p className="font-medium">{activity.method}</p>
                        </div>
                      </div>
                      
                      <div>
                        <div className="flex justify-between text-sm mb-2">
                          <span>Growth Progress</span>
                          <span>{activity.progress}%</span>
                        </div>
                        <Progress value={activity.progress} className="h-2" />
                      </div>
                      
                      <div className="bg-gray-50 dark:bg-gray-800 p-3 rounded-lg">
                        <p className="text-sm">
                          <strong>Seed Source:</strong> {activity.seedSource}
                        </p>
                      </div>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Crop Monitoring Tab */}
        <TabsContent value="monitoring" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>Crop Monitoring</CardTitle>
              <CardDescription>
                Growth tracking with traditional indicators and modern assessment
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {cropMonitoring.map((crop) => (
                  <Card key={crop.id} className="border-2">
                    <CardHeader className="pb-3">
                      <div className="flex items-center justify-between">
                        <CardTitle className="text-lg">{crop.crop}</CardTitle>
                        <Badge variant={
                          crop.health === 'Excellent' ? 'default' :
                          crop.health === 'Good' ? 'secondary' :
                          'destructive'
                        }>
                          {crop.health}
                        </Badge>
                      </div>
                    </CardHeader>
                    <CardContent className="space-y-4">
                      <div className="grid grid-cols-2 md:grid-cols-3 gap-4 text-sm">
                        <div>
                          <span className="text-gray-600">Growth Stage:</span>
                          <p className="font-medium">{crop.stage}</p>
                        </div>
                        <div>
                          <span className="text-gray-600">Last Inspection:</span>
                          <p className="font-medium">{crop.lastInspection}</p>
                        </div>
                        <div className="flex items-center space-x-1">
                          <Thermometer className="h-4 w-4 text-gray-600" />
                          <div>
                            <span className="text-gray-600">Weather:</span>
                            <p className="font-medium">{crop.weatherConditions}</p>
                          </div>
                        </div>
                      </div>
                      
                      <div>
                        <div className="flex justify-between text-sm mb-2">
                          <span>Plant Vigor</span>
                          <span>{crop.vigor}%</span>
                        </div>
                        <Progress value={crop.vigor} className="h-2" />
                      </div>
                      
                      <div className="bg-green-50 dark:bg-green-900/20 p-3 rounded-lg">
                        <p className="text-sm text-green-800 dark:text-green-200">
                          <strong>Traditional Indicators:</strong> {crop.traditionalIndicators}
                        </p>
                      </div>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Pest Management Tab */}
        <TabsContent value="pest" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center space-x-2">
                <Bug className="h-5 w-5" />
                <span>Pest & Disease Management</span>
              </CardTitle>
              <CardDescription>
                Integrated pest management with traditional and modern methods
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {pestManagement.map((pest) => (
                  <Card key={pest.id} className="border-2">
                    <CardHeader className="pb-3">
                      <div className="flex items-center justify-between">
                        <CardTitle className="text-lg">{pest.pest}</CardTitle>
                        <Badge variant={
                          pest.severity === 'Low' ? 'default' :
                          pest.severity === 'Medium' ? 'secondary' :
                          'destructive'
                        }>
                          {pest.severity} Severity
                        </Badge>
                      </div>
                    </CardHeader>
                    <CardContent className="space-y-4">
                      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                        <div>
                          <span className="text-gray-600">Affected Crop:</span>
                          <p className="font-medium">{pest.crop}</p>
                        </div>
                        <div>
                          <span className="text-gray-600">Treatment:</span>
                          <p className="font-medium">{pest.treatment}</p>
                        </div>
                        <div>
                          <span className="text-gray-600">Application Date:</span>
                          <p className="font-medium">{pest.applicationDate}</p>
                        </div>
                        <div>
                          <span className="text-gray-600">Cost:</span>
                          <p className="font-medium">{pest.cost}</p>
                        </div>
                      </div>
                      
                      <div className="flex items-center space-x-2">
                        {pest.effectiveness === 'Excellent' ? (
                          <CheckCircle className="h-5 w-5 text-green-500" />
                        ) : (
                          <AlertTriangle className="h-5 w-5 text-yellow-500" />
                        )}
                        <span className="text-sm">
                          Treatment Effectiveness: <strong>{pest.effectiveness}</strong>
                        </span>
                      </div>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Harvest Tab */}
        <TabsContent value="harvest" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center space-x-2">
                <Scissors className="h-5 w-5" />
                <span>Harvest Management</span>
              </CardTitle>
              <CardDescription>
                Track harvest timing with traditional indicators and moon phases
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="bg-gray-100 dark:bg-gray-800 rounded-lg p-8 text-center">
                <Scissors className="h-16 w-16 mx-auto text-gray-400 mb-4" />
                <h3 className="text-lg font-medium mb-2">Harvest Planning</h3>
                <p className="text-gray-600 dark:text-gray-400 mb-4">
                  Plan and track harvest activities with traditional timing indicators
                </p>
                <Button className="bg-orange-600 hover:bg-orange-700">
                  Plan Harvest
                </Button>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Livestock Tab */}
        <TabsContent value="livestock" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center space-x-2">
                <Heart className="h-5 w-5" />
                <span>Livestock Production</span>
              </CardTitle>
              <CardDescription>
                Track breeding, health, and production with traditional practices
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {livestockProduction.map((animal) => (
                  <Card key={animal.id} className="border-2">
                    <CardHeader className="pb-3">
                      <div className="flex items-center justify-between">
                        <CardTitle className="text-lg">{animal.type} - {animal.breed}</CardTitle>
                        <Badge variant="default">{animal.healthStatus}</Badge>
                      </div>
                    </CardHeader>
                    <CardContent className="space-y-4">
                      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                        <div>
                          <span className="text-gray-600">Count:</span>
                          <p className="font-medium">{animal.count}</p>
                        </div>
                        <div className="flex items-center space-x-1">
                          {animal.type === 'Goats' ? (
                            <Milk className="h-4 w-4 text-gray-600" />
                          ) : (
                            <Egg className="h-4 w-4 text-gray-600" />
                          )}
                          <div>
                            <span className="text-gray-600">Production:</span>
                            <p className="font-medium">
                              {animal.type === 'Goats' ? animal.milkProduction : animal.eggProduction}
                            </p>
                          </div>
                        </div>
                        <div>
                          <span className="text-gray-600">
                            {animal.type === 'Goats' ? 'Last Breeding:' : 'Last Vaccination:'}
                          </span>
                          <p className="font-medium">
                            {animal.type === 'Goats' ? animal.lastBreeding : animal.lastVaccination}
                          </p>
                        </div>
                        <div>
                          <span className="text-gray-600">
                            {animal.type === 'Goats' ? 'Expected Kidding:' : 'Mortality Rate:'}
                          </span>
                          <p className="font-medium">
                            {animal.type === 'Goats' ? animal.expectedKidding : animal.mortalityRate}
                          </p>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Records Tab */}
        <TabsContent value="records" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center space-x-2">
                <BarChart3 className="h-5 w-5" />
                <span>Production Records</span>
              </CardTitle>
              <CardDescription>
                Comprehensive production summary and performance analysis
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <Card className="bg-green-50 dark:bg-green-900/20">
                  <CardContent className="p-4 text-center">
                    <Sprout className="h-8 w-8 mx-auto text-green-600 mb-2" />
                    <h4 className="font-medium text-green-800 dark:text-green-200">
                      Crop Yield
                    </h4>
                    <p className="text-2xl font-bold text-green-600">2.8 tons</p>
                    <p className="text-xs text-green-700 dark:text-green-300">
                      This season
                    </p>
                  </CardContent>
                </Card>
                
                <Card className="bg-blue-50 dark:bg-blue-900/20">
                  <CardContent className="p-4 text-center">
                    <Heart className="h-8 w-8 mx-auto text-blue-600 mb-2" />
                    <h4 className="font-medium text-blue-800 dark:text-blue-200">
                      Livestock Production
                    </h4>
                    <p className="text-2xl font-bold text-blue-600">95%</p>
                    <p className="text-xs text-blue-700 dark:text-blue-300">
                      Health rate
                    </p>
                  </CardContent>
                </Card>
                
                <Card className="bg-orange-50 dark:bg-orange-900/20">
                  <CardContent className="p-4 text-center">
                    <Package className="h-8 w-8 mx-auto text-orange-600 mb-2" />
                    <h4 className="font-medium text-orange-800 dark:text-orange-200">
                      Revenue
                    </h4>
                    <p className="text-2xl font-bold text-orange-600">₦485K</p>
                    <p className="text-xs text-orange-700 dark:text-orange-300">
                      This season
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

