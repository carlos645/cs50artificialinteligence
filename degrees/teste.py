from util import Node, StackFrontier, QueueFrontier
from degrees import load_data,person_id_for_name,neighbors_for_person

#get source id
    sourceid = person_id_for_name(source)
    #get target id
    targetid = person_id_for_name(target)
    #inicialize de stack
    fron = QueueFrontier
    #set the first node
    no = Node(state=sourceid,parent=None,action =people[sourceid]['movies'])
    #put the fisrt node in the frontier
    fron.add(no)
    #set target = false
    target = false
    #array para fazer o caminho inverso.
    path = set()
    
    pile = set()
    for person in people:
        a = Node(state=person["id"],parent = None,action = person['movies'])
        pile.append(a)  
   
    vnode = no
    while(target == False):

        for movie in no.action:
         
            for person in people:
                for vmovie in person['movies']:
                    if(vmovie == movie):
                        cnode = Node(state=person['id'],parent=no,action=person['movies_id'])
                        if(person['id']== targetid):
                            path = cnode
                            target == True
                        if (fron.empty()):
                            raise Exception("Empty frontier")
                        else:
                            fron.add(cnode)
                            no = fron.frontier[0]
                            fron.frontier = fron.frontier[1:]
        
                 
    result = set()
        #se chegou no target. 
    if(path ==None):
        return None
    else:
        while(path):
            movieid = None
            for movie in path.action:
                for nmovie in path.parent.action:
                    if (movie == nmovie):
                        movieid = movie
            result.append(movieid,path.state)
            path = path.parent

    return result