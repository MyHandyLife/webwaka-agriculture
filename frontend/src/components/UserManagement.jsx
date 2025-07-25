import { useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Label } from '@/components/ui/label.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar.jsx'
import { 
  Users, 
  UserPlus, 
  Shield, 
  MapPin, 
  Phone, 
  Globe,
  Crown,
  Heart,
  CheckCircle,
  AlertCircle
} from 'lucide-react'

export function UserManagement() {
  const [activeTab, setActiveTab] = useState('profile')
  const [userProfile, setUserProfile] = useState({
    name: 'Amara Okafor',
    phone: '+234 803 123 4567',
    village: 'Igbo-Ukwu',
    state: 'Anambra',
    country: 'Nigeria',
    language: 'Igbo',
    role: 'Farmer',
    verified: true,
    cooperative: 'Igbo-Ukwu Farmers Cooperative',
    traditionalTitle: 'Eze Ubi (Farm King)'
  })

  const communityMembers = [
    {
      id: 1,
      name: 'Chief Emeka Nwosu',
      role: 'Traditional Authority',
      village: 'Igbo-Ukwu',
      verified: true,
      status: 'online'
    },
    {
      id: 2,
      name: 'Dr. Adaora Okonkwo',
      role: 'Extension Agent',
      village: 'Igbo-Ukwu',
      verified: true,
      status: 'offline'
    },
    {
      id: 3,
      name: 'Chidi Okwu',
      role: 'Farmer',
      village: 'Igbo-Ukwu',
      verified: false,
      status: 'online'
    }
  ]

  const cooperatives = [
    {
      id: 1,
      name: 'Igbo-Ukwu Farmers Cooperative',
      members: 156,
      established: '2018',
      focus: 'Yam and Cassava Production',
      status: 'active'
    },
    {
      id: 2,
      name: 'Anambra Women Farmers Union',
      members: 89,
      established: '2020',
      focus: 'Vegetable Farming',
      status: 'active'
    }
  ]

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white">User Management</h2>
          <p className="text-gray-600 dark:text-gray-400">
            Community-based profiles with traditional authority integration
          </p>
        </div>
        <Button className="bg-blue-600 hover:bg-blue-700">
          <UserPlus className="h-4 w-4 mr-2" />
          Add Member
        </Button>
      </div>

      <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
        <TabsList className="grid w-full grid-cols-4">
          <TabsTrigger value="profile">My Profile</TabsTrigger>
          <TabsTrigger value="community">Community</TabsTrigger>
          <TabsTrigger value="cooperatives">Cooperatives</TabsTrigger>
          <TabsTrigger value="verification">Verification</TabsTrigger>
        </TabsList>

        {/* Profile Tab */}
        <TabsContent value="profile" className="space-y-6">
          <Card>
            <CardHeader>
              <div className="flex items-center space-x-4">
                <Avatar className="h-16 w-16">
                  <AvatarImage src="/api/placeholder/64/64" />
                  <AvatarFallback className="bg-blue-600 text-white text-lg">
                    {userProfile.name.split(' ').map(n => n[0]).join('')}
                  </AvatarFallback>
                </Avatar>
                <div className="flex-1">
                  <div className="flex items-center space-x-2">
                    <CardTitle className="text-xl">{userProfile.name}</CardTitle>
                    {userProfile.verified && (
                      <CheckCircle className="h-5 w-5 text-green-500" />
                    )}
                  </div>
                  <CardDescription className="flex items-center space-x-2">
                    <Crown className="h-4 w-4" />
                    <span>{userProfile.traditionalTitle}</span>
                  </CardDescription>
                </div>
                <Badge variant={userProfile.verified ? "default" : "destructive"}>
                  {userProfile.verified ? "Verified" : "Pending"}
                </Badge>
              </div>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label htmlFor="name">Full Name</Label>
                  <Input 
                    id="name" 
                    value={userProfile.name}
                    onChange={(e) => setUserProfile({...userProfile, name: e.target.value})}
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="phone">Phone Number</Label>
                  <div className="flex items-center space-x-2">
                    <Phone className="h-4 w-4 text-gray-500" />
                    <Input 
                      id="phone" 
                      value={userProfile.phone}
                      onChange={(e) => setUserProfile({...userProfile, phone: e.target.value})}
                    />
                  </div>
                </div>
                <div className="space-y-2">
                  <Label htmlFor="village">Village/Community</Label>
                  <div className="flex items-center space-x-2">
                    <MapPin className="h-4 w-4 text-gray-500" />
                    <Input 
                      id="village" 
                      value={userProfile.village}
                      onChange={(e) => setUserProfile({...userProfile, village: e.target.value})}
                    />
                  </div>
                </div>
                <div className="space-y-2">
                  <Label htmlFor="language">Primary Language</Label>
                  <div className="flex items-center space-x-2">
                    <Globe className="h-4 w-4 text-gray-500" />
                    <select 
                      id="language"
                      value={userProfile.language}
                      onChange={(e) => setUserProfile({...userProfile, language: e.target.value})}
                      className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
                    >
                      <option value="Igbo">Igbo</option>
                      <option value="Yoruba">Yoruba</option>
                      <option value="Hausa">Hausa</option>
                      <option value="English">English</option>
                      <option value="Kiswahili">Kiswahili</option>
                    </select>
                  </div>
                </div>
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="cooperative">Cooperative Membership</Label>
                <Input 
                  id="cooperative" 
                  value={userProfile.cooperative}
                  onChange={(e) => setUserProfile({...userProfile, cooperative: e.target.value})}
                />
              </div>

              <div className="flex justify-end space-x-2">
                <Button variant="outline">Cancel</Button>
                <Button className="bg-blue-600 hover:bg-blue-700">Save Changes</Button>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Community Tab */}
        <TabsContent value="community" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center space-x-2">
                <Users className="h-5 w-5" />
                <span>Community Members</span>
              </CardTitle>
              <CardDescription>
                Connect with farmers, extension agents, and traditional authorities in your area
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {communityMembers.map((member) => (
                  <div key={member.id} className="flex items-center justify-between p-4 border rounded-lg">
                    <div className="flex items-center space-x-3">
                      <Avatar>
                        <AvatarFallback className="bg-gray-600 text-white">
                          {member.name.split(' ').map(n => n[0]).join('')}
                        </AvatarFallback>
                      </Avatar>
                      <div>
                        <div className="flex items-center space-x-2">
                          <h4 className="font-medium">{member.name}</h4>
                          {member.verified && (
                            <CheckCircle className="h-4 w-4 text-green-500" />
                          )}
                        </div>
                        <p className="text-sm text-gray-600 dark:text-gray-400">{member.role}</p>
                        <p className="text-xs text-gray-500">{member.village}</p>
                      </div>
                    </div>
                    <div className="flex items-center space-x-2">
                      <Badge variant={member.status === 'online' ? 'default' : 'secondary'}>
                        {member.status}
                      </Badge>
                      <Button size="sm" variant="outline">
                        <Heart className="h-4 w-4 mr-1" />
                        Connect
                      </Button>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Cooperatives Tab */}
        <TabsContent value="cooperatives" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>Farmer Cooperatives</CardTitle>
              <CardDescription>
                Join or manage farmer cooperatives in your region
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {cooperatives.map((coop) => (
                  <Card key={coop.id} className="border-2">
                    <CardHeader className="pb-3">
                      <div className="flex items-center justify-between">
                        <CardTitle className="text-lg">{coop.name}</CardTitle>
                        <Badge variant="default">{coop.status}</Badge>
                      </div>
                    </CardHeader>
                    <CardContent className="space-y-2">
                      <div className="flex justify-between text-sm">
                        <span className="text-gray-600">Members:</span>
                        <span className="font-medium">{coop.members}</span>
                      </div>
                      <div className="flex justify-between text-sm">
                        <span className="text-gray-600">Established:</span>
                        <span className="font-medium">{coop.established}</span>
                      </div>
                      <div className="text-sm">
                        <span className="text-gray-600">Focus:</span>
                        <p className="font-medium">{coop.focus}</p>
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

        {/* Verification Tab */}
        <TabsContent value="verification" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center space-x-2">
                <Shield className="h-5 w-5" />
                <span>Farmer Verification</span>
              </CardTitle>
              <CardDescription>
                Verify your identity and farming experience for community trust
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-4">
                  <div className="flex items-center justify-between p-4 border rounded-lg">
                    <div>
                      <h4 className="font-medium">Identity Verification</h4>
                      <p className="text-sm text-gray-600">Phone number and basic info</p>
                    </div>
                    <CheckCircle className="h-6 w-6 text-green-500" />
                  </div>
                  
                  <div className="flex items-center justify-between p-4 border rounded-lg">
                    <div>
                      <h4 className="font-medium">Farming Experience</h4>
                      <p className="text-sm text-gray-600">Years of farming experience</p>
                    </div>
                    <CheckCircle className="h-6 w-6 text-green-500" />
                  </div>
                  
                  <div className="flex items-center justify-between p-4 border rounded-lg">
                    <div>
                      <h4 className="font-medium">Community Endorsement</h4>
                      <p className="text-sm text-gray-600">Traditional authority approval</p>
                    </div>
                    <AlertCircle className="h-6 w-6 text-yellow-500" />
                  </div>
                </div>
                
                <div className="space-y-4">
                  <Card className="bg-green-50 dark:bg-green-900/20">
                    <CardContent className="p-4">
                      <div className="flex items-center space-x-2 mb-2">
                        <CheckCircle className="h-5 w-5 text-green-500" />
                        <h4 className="font-medium text-green-800 dark:text-green-200">
                          Verification Complete
                        </h4>
                      </div>
                      <p className="text-sm text-green-700 dark:text-green-300">
                        Your farmer profile has been verified by the community. 
                        You can now access all WebWaka features.
                      </p>
                    </CardContent>
                  </Card>
                  
                  <div className="space-y-2">
                    <Label>Traditional Authority Contact</Label>
                    <Input placeholder="Chief Emeka Nwosu" disabled />
                  </div>
                  
                  <div className="space-y-2">
                    <Label>Verification Date</Label>
                    <Input placeholder="March 15, 2024" disabled />
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  )
}

