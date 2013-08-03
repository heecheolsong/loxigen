package org.openflow.protocol.ver11;

import org.jboss.netty.buffer.ChannelBuffer;
import org.openflow.exceptions.OFParseError;
import org.openflow.protocol.OFBsnVportQInQ;
import org.openflow.protocol.OFMatchBmap;
import org.openflow.protocol.match.Match;


/**
 * Collection of helper functions for reading and writing into ChannelBuffers
 *
 * @author capveg
 */

public class ChannelUtilsVer11 {
    public static Match readOFMatch(final ChannelBuffer bb) throws OFParseError {
        return OFMatchV2Ver11.READER.readFrom(bb);
    }

    // TODO these need to be figured out / removed
    public static OFBsnVportQInQ readOFBsnVportQInQ(ChannelBuffer bb) {
        throw new UnsupportedOperationException("not implemented");
    }

    public static void writeOFBsnVportQInQ(ChannelBuffer bb,
            OFBsnVportQInQ vport) {
        throw new UnsupportedOperationException("not implemented");
    }


    public static OFMatchBmap readOFMatchBmap(ChannelBuffer bb) {
        throw new UnsupportedOperationException("not implemented");
    }

    public static void writeOFMatchBmap(ChannelBuffer bb, OFMatchBmap match) {
        throw new UnsupportedOperationException("not implemented");
    }
}
