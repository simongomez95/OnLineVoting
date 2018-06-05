package identifier.Logic;

import identifier.Repository.Entities.Identifier;
import identifier.Repository.IdentifierRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class IdentifierService {

    @Autowired
    IdentifierRepository idRepo;

    public Optional<Identifier> saveNonce(Identifier identifier){
        try{
            identifier.setId(null);
            idRepo.saveAndFlush(identifier);
            return Optional.of(identifier);
        } catch (Exception e){
            System.out.print(e);
            return Optional.empty();
        }
    }

    public Optional<Identifier> getNonce(long id){
        try{
            Identifier identifier = idRepo.findOne(id);
            if (identifier!= null) {
                return Optional.of(identifier);
            } else {
                return Optional.empty();
            }
        } catch (Exception e) {
            System.out.print(e);
            return Optional.empty();
        }
    }
}